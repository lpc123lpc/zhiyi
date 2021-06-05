from sklearn.model_selection import train_test_split as holdout
import joblib
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd


if __name__ == '__main__':
    pathHead = "../database/static/trainCsv/"
    pathTail = ".csv"
    targetPathHead = '../saved_model/'
    targetPathTail = '.pkl'

    for i in range(1, 1049):
        print(i)
        path = pathHead + str(i) + pathTail
        df = pd.read_csv(path)

        features = df.drop(['num'], axis=1)
        # features = features.drop(['n'], axis=1)
        features = features.drop(['time'], axis=1)
        targets = df['num']
        x_train, x_test, y_train, y_test = holdout(features, targets, test_size=0.1, random_state=0)

        dis_knr = KNeighborsRegressor(weights='distance')
        dis_knr.fit(x_train, y_train)
        # dis_knr_y_predict = dis_knr.predict(x_test)
        targetPath = targetPathHead + str(i) + targetPathTail
        joblib.dump(dis_knr, targetPath)


