import math

def sigmoid(Z):
   
    return 1 / (1 + math.exp(-Z))
    
   
def WeightedSum(Input,weight,Bias):
   
   Z = sum(w *x for x, w in zip(Input,weight)) + Bias
   Z_hat = sigmoid(Z)
   return Z , Z_hat
   
   
def main():

  Input = [2,3]
  weight = [0.4,0.6]
  Bias = 0.5
  Z , Z_hat = WeightedSum(Input,weight,Bias)

  print("Weighted sum:",Z)
  print("Outpu after activatuion function :",Z_hat)


if __name__ =="__main__":
    main()