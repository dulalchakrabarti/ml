from zoo.chronos.data import TSDataset
from sklearn.preprocessing import StandardScaler

tsdata_train, tsdata_valid, tsdata_test = TSDataset.from_pandas(df, dt_col="timestamp", target_col="value",
                                                                with_split=True, val_ratio=0.1, test_ratio=0.1)
lookback, horizon = 6, 1

scaler = StandardScaler()
for tsdata in [tsdata_train, tsdata_valid, tsdata_test]:
    tsdata.deduplicate().impute().gen_dt_feature()\
          .scale(scaler, fit=(tsdata is tsdata_train))\
          .roll(lookback=lookback, horizon=horizon)                                                                
x, y = tsdata_train.to_numpy() 
x_val, y_val = tsdata_valid.to_numpy() 
# x.shape = (num of sample, lookback, num of input feature)
# y.shape = (num of sample, horizon, num of output feature)

forecaster = TCNForecaster(past_seq_len=lookback,  # number of steps to look back
                           future_seq_len=horizon,  # number of steps to predict
                           input_feature_num=x.shape[-1],  # number of feature to use
                           output_feature_num=y.shape[-1])  # number of feature to predict
res = forecaster.fit(x, y, validation_data=(x_val, y_val), epochs=3)
x_test, y_test = tsdata_test.to_numpy()
pred = forecaster.predict(x_test)
pred_unscale, groundtruth_unscale = tsdata_test.unscale_numpy(pred), tsdata_test.unscale_numpy(y_test)
forecaster.save("nyc_taxi.fxt")
forecaster.restore("nyc_taxi.fxt")

