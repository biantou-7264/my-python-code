from psutil import sensors_battery,POWER_TIME_UNLIMITED
testba=False
testbai=0
testpo=False
testpoi=0
def battery():
    global testba,testbai
    if testba:
        return testbai
    else:
        sensor=sensors_battery()
        if sensor is None:
            return 0
        else:
            return sensor.percent
def power():
    global testpo,testpoi
    if testpo:
        return testpoi
    else:
        sensor=sensors_battery()
        if sensor is None:
            return False
        else:
            return sensor.power_plugged
def time(format=False):
    sensor=sensors_battery()
    if power():
        if sensor.secsleft!=POWER_TIME_UNLIMITED:
            hr=sensor.secsleft//3600
            mi=(sensor.secsleft%3600)//60
            if format:
                return '%d:%d'% (hr,mi)
            else:
                return (hr,mi)
        else:
            if format:
                return '--:--'
            else:
                return ('--','--')
    else:
        if format:
            return '--:--'
        else:
            return ('--','--')
def canuse():
    sensor=sensors_battery()
    return sensor is not None
def test():
    print('电量:%.1f'% battery())
    if power():
        print('当前正在充电')
    else:
        print('当前不在充电')
    print('还剩%s充满'% time(True))
if __name__=='__main__':
    test()