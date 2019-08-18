import wfdb
import pandas as pd

from qrs_detection import QRSDetectorOffline

# record = wfdb.rdrecord('mit-bih-arrhythmia-database/100', sampto=3000)
# print(record.p_signal[0,0])
# ann = wfdb.rdann('mit-bih-arrhythmia-database/100', 'atr', sampto = 300000)
# print(ann.symbol)
# pd.DataFrame(record.p_signal[:, 1]).to_csv("foo.csv")


DS1=[101, 106, 108, 109, 112, 114, 115, 116, 118,119, 122, 124, 201, 203, 205, 207, 208, 209, 215, 220, 223,230]


def convert_data(sampto=3000):
    for file in DS1:
        record = wfdb.rdrecord('mit-bih-arrhythmia-database-1.0.0 2/' + str(file), sampto=sampto)
        pd.DataFrame(record.p_signal[:, 0]).to_csv("temp.csv")
        QRSDetectorOffline(ecg_data_path="temp.csv", verbose=True,
                                      log_data=True, plot_data=True, show_plot=False)


if __name__ == "__main__":
    convert_data()


