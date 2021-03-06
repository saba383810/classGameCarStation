import time

# クラスの定義
class CarException(Exception):
    def __init__(self,bv):
        self.badValue = bv

class Car:
    #コンストラクタ
    def __init__(self,capacity,gas):
        self.__capacity = capacity
        self.__gas = gas
        print("\n車を作成しました。\n")
        time.sleep(1)

    def getCapacity(self):
        return self.__capacity
    def getGas(self):
        return self.__gas

    def setGas(self,gas):
        if gas <= 0:
            raise(CarException(gas))
        self.__gas += gas
        time.sleep(1)
        print("\n給油が完了しました。\n")
        time.sleep(1)

    def useGas(self):
        self.__gas -= 10
        time.sleep(1)
        print("\nあなたはドライブを楽しみ10リットル消費した。\n")
        time.sleep(1)

    def show(self):
        print("定員 : ",self.getCapacity(),"人","\nガソリン量 : ",self.getGas(),"リットル")
        time.sleep(1)

class Track(Car):

    def __init__(self,cap,gs):
        super().__init__(cap,gs)
        
        self.__burden = 0
        print("\nトラックを作成しました。\n")
        time.sleep(1)
    
    def addBurden(self):
        self.__burden += 10
        time.sleep(1)
        print("\n積荷が完了しました。")
        time.sleep(1)
    
    def getBurden(self):
        return self.__burden

    def show(self):
        print("\nトラックの状態:\n\n        定員 : ",self.getCapacity(),"人","\n  ガソリン量 : ",self.getGas(),"リットル","\n    積荷の量 : ",self.getBurden(),"トン")
        time.sleep(1)

#メイン処理
print("\nこんにちは！カーステーションにようこそ！\n")
time.sleep(0.5)
track = Track(3,10)
while 1:

    num = int(input("\nここで何を行いますか？\n\n  1:現在の状態を見る\n  2:積荷に荷物を入れる\n  3:給油する\n  4:走行する\n  5:終了\n\n1~5までの数字を入力してください。>>"))
    if num == 1:
        track.show()
    elif num == 2:
        track.addBurden()
    elif num == 3:      
        num2 =int(input("何リットル入れますか？"))
        try:
            track.setGas(num2)
        except CarException as e:
            print("\n0より小さい値は給油できません。")
            print("給油しようとした値は、",e.badValue,"です。")
            print("0より大きい値を入れてください")
            time.sleep(1)

    elif num == 4:
        track.useGas()
        g = track.getGas()
        if(g<=0):
            print("\nガソリンがなくなりました！",end="")
            break
    elif num == 5:
        break
    else :
        print("\n          正 し い 数 字 を 入 力 し て く だ さ い ! ")
        
print("ご利用ありがとうございました。\n")
time.sleep(1)
    
