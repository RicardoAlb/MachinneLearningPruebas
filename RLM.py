from sklearn.model_selection import train_test_split
import ObtenciónDatos
#   ºimport sklearn.model_selection import kl


x=ObtenciónDatos.df_rsi["bitcoin"].values.reshape(-1,1)
y=ObtenciónDatos.df_precio["bitcoin"].values.reshape(-1,1)

X_train, X_test, y_train_ , y_test=train_test_split(x, y, test_size=0.33, random_state=100)

print("df:", ObtenciónDatos.df_precio.shape)
print("x:", x.shape)
print("X train:", X_train.shape)
print("X test", X_test.shape)