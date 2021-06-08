from sklearn.model_selection import train_test_split as holdout
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.neighbors import KNeighborsRegressor
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['PingFang HK']
    plt.rcParams['axes.unicode_minus'] = False

    df = pd.read_csv('China.csv')
    df.head()

    features = df.drop(['num'], axis=1)
    features = features.drop(['n'], axis=1)
    features = features.drop(['time'], axis=1)
    targets = df['num']
    x_train, x_test, y_train, y_test = holdout(features, targets, test_size=0.1, random_state=0)

    Lin_reg_model = LinearRegression()
    Lin_reg_model.fit(x_train, y_train)

    print('Intercept:', Lin_reg_model.intercept_)
    print('Coefficients:', Lin_reg_model.coef_)

    Lin_reg_model_train_pred = Lin_reg_model.predict(x_train)
    Lin_reg_model_test_pred = Lin_reg_model.predict(x_test)

    # Mean squared error
    Lin_reg_model_train_mse = mean_squared_error(y_train, Lin_reg_model_train_pred)
    Lin_reg_model_test_mse = mean_squared_error(y_test, Lin_reg_model_test_pred)
    print('MSE train data: {:.3}, \nMSE test data: {:.3}\n'.format(Lin_reg_model_train_mse, Lin_reg_model_test_mse))

    # Root Mean Squared error
    print('RMSE train data: {:.3}, \nRMSE test data: {:.3}\n'.format(
        np.sqrt(np.absolute(Lin_reg_model_train_mse)),
        np.sqrt(np.absolute(Lin_reg_model_train_mse))))

    # R^2 - coefficient of determination
    print('R2 train data: {:.3}, \nR2 test data: {:.3}\n'.format(
        r2_score(y_train, Lin_reg_model_train_pred),
        r2_score(y_test, Lin_reg_model_test_pred)))

    # Model Score
    print('Model Score:', Lin_reg_model.score(x_test, y_test))

    plt.subplot(531)
    plt.title("线性回归")
    plt.plot(features, targets)
    plt.plot(features, Lin_reg_model.predict(features))

    # 多项式回归
    model = pl.make_pipeline(
        # 10: 多项式的最高次数
        sp.PolynomialFeatures(9),  # 多项式特征扩展器
        lm.LinearRegression())  # 线性回归器

    # 训练模型
    model.fit(x_train, y_train)
    # 求预测值y
    # y_test = model.predict(x_test)

    # 模型评估
    print('Model Score:', model.score(x_test, y_test))
    plt.subplot(533)
    plt.title("多项式回归")
    plt.plot(features, targets)
    plt.plot(features, model.predict(features))

    list = np.array([[487]])
    print(model.predict(list))

    # 支持向量机
    # 线性核函数
    linear_svr = SVR(kernel='linear')
    linear_svr.fit(x_train, y_train)
    linear_svr_y_pred = linear_svr.predict(x_test)
    print("线性核函数")
    print('Model Score:', linear_svr.score(x_test, y_test))
    print(linear_svr.predict(list))
    plt.subplot(537)
    plt.title("SVM线性")
    plt.plot(features, targets)
    plt.plot(features, linear_svr.predict(features))

    # 多项式核函数
    poly_svr = SVR(kernel='poly')
    poly_svr.fit(x_train, y_train)
    poly_svr_y_pred = poly_svr.predict(x_test)
    print("多项式核函数")
    print('Model Score:', poly_svr.score(x_test, y_test))
    print(poly_svr.predict(list))
    plt.subplot(539)
    plt.title("SVM多项式")
    plt.plot(features, targets)
    plt.plot(features, poly_svr.predict(features))

    uni_knr = KNeighborsRegressor(weights='uniform')
    uni_knr.fit(x_train, y_train)
    uni_knr_y_predict = uni_knr.predict(x_test)
    print("k近邻1")
    print('Model Score:', poly_svr.score(x_test, y_test))
    print(uni_knr.predict(list))
    plt.subplot(5, 3, 13)
    plt.title("K近邻1")
    plt.plot(features, targets)
    plt.plot(features, uni_knr.predict(features))

    dis_knr = KNeighborsRegressor(weights='distance')
    dis_knr.fit(x_train, y_train)
    dis_knr_y_predict = dis_knr.predict(x_test)
    joblib.dump(dis_knr, '../saved_model/rfc.pkl')
    # load model
    rfc2 = joblib.load('../saved_model/rfc.pkl')
    print("k近邻2")
    print('Model Score:', poly_svr.score(x_test, y_test))
    print(dis_knr.predict(list))
    plt.subplot(5, 3, 15)
    plt.title("K近邻2")
    plt.plot(features, targets)
    plt.plot(features, uni_knr.predict(features))
    plt.show()

