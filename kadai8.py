# クラスの定義
class Car:
    #コンストラクタ
    def __init__(self,capacity,gas):
        self.__capacity = capacity
        self.__gas = gas
        print("\n車を作成しました。\n")

    def getCapacity(self):
        return self.__capacity
    def getGas(self):
        return self.__gas

    def setGas(self,gas):
        self.__gas += gas
        print("\n給油が完了しました。\n")

    def useGas(self):
        self.__gas -= 10
        print("\nあなたはドライブを楽しみ10リットル消費した。\n")

    def show(self):
        print("定員 : ",self.getCapacity(),"人","\nガソリン量 : ",self.getGas(),"リットル")

class Track(Car):

    def __init__(self,cap,gs):
        super().__init__(cap,gs)
        
        self.__burden = 0
        print("\nトラックを作成しました。\n")
    
    def addBurden(self):
        self.__burden += 10
        print("\n積荷が完了しました。")
    
    def getBurden(self):
        return self.__burden


    def show(self):
        print("\n現在の状態は\n  定員 : ",self.getCapacity(),"人","\n  ガソリン量 : ",self.getGas(),"リットル","  積荷の量 :",self.getBurden(),"トン\nです")

#インスタンス化

print("\nこんにちは！カーステーションにようこそ！\n")
track = Track(3,10)
while 1:

    num = int(input("\nここで何を行いますか？\n\n  1:現在の状態を見る\n  2:積荷に荷物を入れる\n  3:給油する\n  4:走行する\n  5:終了\n\n1~5までの数字を入力してください。>>"))
    if num == 1:
        track.show()
    elif num == 2:
        track.addBurden()
    elif num == 3:      
        num2 =int(input("何リットル入れますか？"))
        track.setGas(num2)
    elif num == 4:
        track.useGas()
        g = track.getGas()
        if(g<0):
            print("\nガソリンがなくなりました！ご利用ありがとうございました。")
            break
    elif num == 5:
        break
    else :
        print("\n          正 し い 数 字 を 入 力 し て く だ さ い ! ")
    