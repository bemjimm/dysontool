def 计算设备数量(原料供应速度_每分钟, 传送带负载能力_每秒, 冶炼所需物料数量, 冶炼时间_秒):
    # convert supply speed to per second
    原料供应速度_每秒 = 原料供应速度_每分钟 / 60
    
    # smelting machine takes n items every m seconds
    设备每秒需要的原料 = 冶炼所需物料数量 / 冶炼时间_秒
    
    # calculate the number of raw materials can be provided by the conveyor belt in one smelting cycle
    冶炼周期内传送带提供的原料 = 传送带负载能力_每秒 * 冶炼时间_秒

    # calculate the maximum number of devices that can be supported by the supply and conveyor belt speed
    设备数量_供应限制 = 原料供应速度_每秒 / 设备每秒需要的原料
    设备数量_传送带限制 = 冶炼周期内传送带提供的原料 / 设备每秒需要的原料
    实际设备数量 = min(设备数量_供应限制, 设备数量_传送带限制)
    理想设备数量 = max(设备数量_供应限制, 设备数量_传送带限制)
    if 设备数量_供应限制 > 设备数量_传送带限制:
        print("短板在于传送带，实际上能够支撑的设备是%d个，理论设备数量是%d"%(实际设备数量,理想设备数量))
    else:
        print("短板在于原料，实际上能够支撑的设备是%d个，理论设备数量是%d"%(实际设备数量,理想设备数量))
    # the actual number of devices is the minimum of the two
    return 实际设备数量

# test the function
原料供应速度_每分钟 = 3000
传送带负载能力_每秒 = 30
冶炼所需物料数量 = 12
冶炼时间_秒 = 4
计算设备数量(原料供应速度_每分钟, 传送带负载能力_每秒, 冶炼所需物料数量, 冶炼时间_秒)
