from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom

import openpyxl
removed_duplicacy_list=[]
Testtcase_list=[]
varient_list=[]
faltu_list=[]
my_try_list_cmd=[[]]
my_try_list_data=[[]]
preperation_list=[['BufferDTCList','BufferDTCStatusList','loop_idx'],['NotAssigned','NotAssigned','0']]
main_func_j=0
global_j = 0
comd_val=''
value_val=''
DTC_value=''
check_while_case_active=0

if_case_check_active=0
global_local_variant_i=0
check_constraints_start_active=0
check_for_loop_start_active=0
check_DLC_check_start_active=0
#############xml object decleration##############
global testgroup
global testcase
global description
global preparation
global body
global if_body
global constraints_start
global for_loop_start
global DLC_check_start
wb = openpyxl.load_workbook('Sample_TDP.xlsx')
type(wb)
sheet = wb.get_sheet_by_name("Template")

#################v2.0#################################


def Range_check(local_Range_check):
    #global local_Range_check
    print("Range_check")
    local_Range_check1, local_Range_check2 = local_Range_check.split('=')
    local_Range_check3,local_Range_check4=local_Range_check1.split('::')
    local_Range_check5,local_Range_check6=local_Range_check2.split(':')
    if(local_Range_check3=='sysvar'):
        statecheck = etree.SubElement(testcase, "statecheck")#fixed
        statecheck.set('title', 'Response time check')#fixed
        statecheck.set('wait', '0')#fixed
        expected = etree.SubElement(statecheck, "expected")#fixed
        sysvar = etree.SubElement(expected, "sysvar")#fixed
        sysvar.set('name', local_Range_check3)#fixed
        sysvar.set('namespace', 'Ta')#fixed
        range = etree.SubElement(sysvar, "range")#fixed
        from1 = etree.SubElement(range, "from")#fixed
        to = etree.SubElement(range, "to")#fixed
        from1.text = str(local_Range_check5)  # fixed
        to.text=str(local_Range_check6)#fixed
    elif(local_Range_check3=='envvar'):
        statecheck = etree.SubElement(testcase, "statecheck")  # fixed need to chech whicle execution if i need to use statecheck1 insted of statecheck as i used it earlier
        statecheck.set('title', 'Response time check')  # fixed
        statecheck.set('wait', '0')  # fixed
        expected = etree.SubElement(statecheck, "expected")  # fixed
        envvar = etree.SubElement(expected, "envvar")  # fixed
        envvar.set('name',local_Range_check4)  # varible
        range = etree.SubElement(envvar, "range")  # fixed
        from1 = etree.SubElement(range, "from")#fixed
        from1.text=str(local_Range_check5)#fixed
        to = etree.SubElement(range, "to")#fixed
        to.text=str(local_Range_check6)#fixed
    else:
        pass
    return

def IGN_OFF_ShutDown(local_IGN_OFF_ShutDown):
    print('IGN_OFF_Wakeup')
    IGN_OFF_ShutDown = etree.SubElement(testcase, "capltestfunction")
    IGN_OFF_ShutDown.set('name', 'StateSignal_IGN_OFF_ShutDown')
    IGN_OFF_ShutDown.set('title', 'IGN_OFF')
    
    return


def IGN_ON_ShutDown(local_IGN_ON_ShutDown):
    print('IGN_ON_ShutDown')
    IGN_ON_ShutDown = etree.SubElement(testcase, "capltestfunction")
    IGN_ON_ShutDown.set('name', 'StateSignal_IGN_ON_ShutDown')
    IGN_ON_ShutDown.set('title', 'IGN_ON')
    
    return




def IGN_OFF_Wakeup(local_IGN_OFF_Wakeup):
    print('IGN_OFF_Wakeup')
    IGN_OFF_Wakeup = etree.SubElement(testcase, "capltestfunction")
    IGN_OFF_Wakeup.set('name', 'StateSignal_IGN_OFF_Wakeup')
    IGN_OFF_Wakeup.set('title', 'IGN_OFF')
    
    return


def IGN_ON_Wakeup(local_IGN_ON_Wakeup):
    print('IGN_ON_Wakeup')
    IGN_ON_Wakeup = etree.SubElement(testcase, "capltestfunction")
    IGN_ON_Wakeup.set('name', 'StateSignal_IGN_ON_Wakeup')
    IGN_ON_Wakeup.set('title', 'IGN_ON')
    
    return


def Power_supply_OFF(local_Power_supply_OFF):
    print('Power_supply_OFF')
    Power_supply_OFF = etree.SubElement(testcase, "capltestfunction")
    Power_supply_OFF.set('name', 'OUTPUT_ENABLE_OFF')
    Power_supply_OFF.set('title', 'Power supply OFF')
    
    return

def Power_supply_ON(local_Power_supply_ON):
    print('Power_supply_ON')
    Power_supply_ON = etree.SubElement(testcase, "capltestfunction")
    Power_supply_ON.set('name', 'OUTPUT_ENABLE_ON')
    Power_supply_ON.set('title', 'Power supply ON')
    
    return


def DLC_check_stop(local_DLC_check_stop):
    print('DLC_check_stop')
    global check_DLC_check_start_active
    check_DLC_check_start_active =0
    return

def DLC_check(local_DLC_check):
    print('DLC_check')
    global check_DLC_check_start_active
    global DLC_check_start
    if check_DLC_check_start_active==1:

        DLC_check = etree.SubElement(DLC_check_start, "dlc_ok")
        DLC_check.set('title', 'DLC Check')
        DLC_check.set('dir', 'tx')
        canmsg = etree.SubElement(DLC_check, "canmsg")
        canmsg.set('id',local_DLC_check)
        canmsg.set('bus', 'Main CAN')
    else:
        pass
    return

def DLC_check_start(local_DLC_check_start):
    print('DLC_check_start')
    global check_DLC_check_start_active
    global DLC_check_start
    check_DLC_check_start_active=1
    DLC_check_start = etree.SubElement(testcase, "conditions")
    return


def for_loop_stop(local_for_loop_start):
    print('for_loop_stop')
    global check_for_loop_start_active
    check_for_loop_start_active =0
    return



def Check_signal(local_Check_signal):
    print('Check_signal')
    global for_loop_start
    global check_for_loop_start_active
    local_Check_signal_list=[]
    local_Check_signal_list=local_Check_signal.split('=')
    if check_for_loop_start_active==1:
        Check_signal = etree.SubElement(for_loop_start, "statecheck")
        Check_signal.set('title', 'Signal value check')
        Check_signal.set('wait', '0')
        expected = etree.SubElement(Check_signal, "expected")
        cansignal = etree.SubElement(expected, "cansignal")
        cansignal.set('name', local_Check_signal_list[0])
        cansignal.text=local_Check_signal_list[1]
    else:
        pass


    return

def for_loop_start(local_for_loop_start):
    print('for_loop_start')
    global check_for_loop_start_active
    global for_loop_start
    check_for_loop_start_active=1
    for_loop_start_list=[]
    for_loop_start_list=local_for_loop_start.split(':')

    for_loop_start = etree.SubElement(testcase, "for_loop")
    for_loop_start.set('title', 'Monitoring')
    for_loop_start.set('loopvar', 'loop_idx')
    for_loop_start.set('startvalue', for_loop_start_list[0])
    for_loop_start.set('stopvalue', for_loop_start_list[1])
    for_loop_start.set('increment', for_loop_start_list[2])
    return




def Message_Stop(local_Message_Stop):
    print('Message_Stop')
    Message_Stop = etree.SubElement(testcase, "set")
    Message_Stop.set('title', 'set Message_Stop')
    envvar = etree.SubElement(Message_Stop, "envvar")
    envvar.set('name', 'Message_Send_'+local_Message_Stop)
    envvar.text='0'
    return

def Generate_increasing_high_priority_bus_load_on_all_CAN_channels(local_Generate_increasing_high_priority_bus_load_on_all_CAN_channels):
    print('Generate_increasing_high_priority_bus_load_on_all_CAN_channels')
    Generate_increasing_high_priority_bus_load_on_all_CAN_channels = etree.SubElement(testcase, "set")
    Generate_increasing_high_priority_bus_load_on_all_CAN_channels.set('title', 'Increasing bus load with high priority message on all CAN channels')
    sysvar = etree.SubElement(Generate_increasing_high_priority_bus_load_on_all_CAN_channels, "sysvar")
    sysvar.set('name', 'HighBusLoadTestMode')
    sysvar.set('namespace', 'Ta')
    sysvar.text = '9'
    return


def constraints_stop(local_constraints_stop):
    print('constraints_stop')
    global check_constraints_start_active
    check_constraints_start_active =0

    return

def constraints_start(local_constraints_start):
    global check_constraints_start_active
    global constraints_start
    print('constraints_start')
    check_constraints_start_active=1
    constraints_start = etree.SubElement(testcase, "constraints")
    return


def cycletime(local_cycletime):
    print('cycletime')
    global constraints_start
    global check_constraints_start_active
    cycletime_local_list = []
    cycletime_local_list1=[]
    cycletime_local_list=local_cycletime.split('=')
    cycletime_local_list1=cycletime_local_list[1].split(':')
    if(check_constraints_start_active==1):
        cycletime_abs = etree.SubElement(constraints_start, "cycletime_abs")
        cycletime_abs.set('title', 'Cycle Time Check')
        cycletime_abs.set('min', cycletime_local_list1[0])
        cycletime_abs.set('max', cycletime_local_list1[1])
        cycletime_abs.set('variants', str(varient_list[global_local_variant_i]))
        canmsg = etree.SubElement(cycletime_abs, "canmsg")
        canmsg.set('id', cycletime_local_list[0])
        canmsg.set('bus','Main CAN')


    return



def Stop_generating_bus_load_test_message(local_Stop_generating_bus_load_test_message):
    print('Stop_generating_bus_load_test_message')
    Stop_generating_bus_load_test_message = etree.SubElement(testcase, "set")
    Stop_generating_bus_load_test_message.set('title', 'Stop bus load test message generation')
    sysvar = etree.SubElement(Stop_generating_bus_load_test_message, "sysvar")
    sysvar.set('name', 'HighBusLoadTestMode')
    sysvar.set('namespace', 'Ta')
    sysvar.text='0'
    return


def Stop_ESC_Tx_monitoring(local_Stop_ESC_Tx_monitoring):
    print('Stop_ESC_Tx_monitoring')
    Stop_ESC_Tx_monitoring = etree.SubElement(testcase, "capltestfunction")
    Stop_ESC_Tx_monitoring.set('name', 'StopEscTxMonitoring')
    Stop_ESC_Tx_monitoring.set('title', 'Reset variables to stop ESC Tx Monitoring')
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set delay')
    wait.set('time', '500us')

    return


def Check_value(local_Check_value ):
    print('Check_value')
    Check_value_local_list=[]
    Check_value_local_list1=[]
    Check_value_local_list2=[]
    Check_value_local_list=local_Check_value.split('=') #split signal and value based on =
    if ':'in Check_value_local_list[1]:
        Check_value_local_list2=Check_value_local_list[1].split(':')# split signal based in : for numaric value
        Check_value_local_list1=Check_value_local_list[0].split('::') #split message based on :: ffor signal name
        if(Check_value_local_list1[0]=='sysvar'):
            Check_value = etree.SubElement(testcase, "statecheck")
            Check_value.set('title', 'System variable value check')
            Check_value.set('wait', '0')
            expected = etree.SubElement(Check_value, "expected")
            sysvar = etree.SubElement(expected, "sysvar")
            sysvar.set('name', Check_value_local_list1[2])
            sysvar.set('namespace', Check_value_local_list1[1])

            range = etree.SubElement(sysvar, "range")
            from1 = etree.SubElement(range, "from")
            from1.text=str(Check_value_local_list2[0])
            to = etree.SubElement(range, "to")
            to.text = str(Check_value_local_list2[1])
            print('inside sysvar__:')
        elif(Check_value_local_list1[0]=='envvar'):
            if(len(Check_value_local_list1)=='3'):
                Check_value = etree.SubElement(testcase, "set")
                Check_value.set('title','check envvar value')
                envvar = etree.SubElement(Check_value, "envvar")
                envvar.set('name', Check_value_local_list1[2]+Check_value_local_list1[1])
                range = etree.SubElement(envvar, "range")
                from1 = etree.SubElement(range, "from")
                from1.text = str(Check_value_local_list2[0])
                to = etree.SubElement(range, "to")
                to.text = str(Check_value_local_list2[1])
                print('inside envvar_len3_:')
            elif(len(Check_value_local_list1)=='2'):
                Check_value = etree.SubElement(testcase, "set")
                Check_value.set('title', 'check envvar value')
                envvar = etree.SubElement(Check_value, "envvar")
                envvar.set('name', Check_value_local_list1[1])
                range = etree.SubElement(envvar, "range")
                from1 = etree.SubElement(range, "from")
                from1.text = str(Check_value_local_list2[0])
                to = etree.SubElement(range, "to")
                to.text = str(Check_value_local_list2[1])
                print('inside envvar_len2_:')
            else:
                pass
        else:
            pass
    else:
        Check_value_local_list1 = Check_value_local_list[0].split('::')
        if (Check_value_local_list1[0] == 'sysvar'):
            Check_value = etree.SubElement(testcase, "statecheck")
            Check_value.set('title', 'System variable value check')
            Check_value.set('wait', '0')
            expected = etree.SubElement(Check_value, "expected")
            sysvar = etree.SubElement(expected, "sysvar")
            sysvar.set('name', Check_value_local_list1[2])
            sysvar.set('namespace', Check_value_local_list1[1])
            sysvar.text=str(Check_value_local_list[1])
            print('inside sysvar__=')
        elif (Check_value_local_list1[0] == 'envvar'):
            if (len(Check_value_local_list1) == '3'):
                Check_value = etree.SubElement(testcase, "set")
                Check_value.set('title', 'check envvar value')
                envvar = etree.SubElement(Check_value, "envvar")
                envvar.set('name',Check_value_local_list1[2]+Check_value_local_list1[1])
                envvar.text=str(Check_value_local_list[1])
                print('inside envvar_len3_=')
                pass
            elif (len(Check_value_local_list1) == '2'):
                Check_value = etree.SubElement(testcase, "set")
                Check_value.set('title', 'check envvar value')
                envvar = etree.SubElement(Check_value, "envvar")
                envvar.set('name',Check_value_local_list1[1])
                envvar.text = str(Check_value_local_list[1])
                print('inside envvar_len3_=')
            else:
                pass
        else:
            pass

    return

def Start_ESC_Tx_monitoring(local_Start_ESC_Tx_monitoring):
    print('Start_ESC_Tx_monitoring')
    Start_ESC_Tx_monitoring = etree.SubElement(testcase, "capltestfunction")
    Start_ESC_Tx_monitoring.set('name', 'StartEscTxMonitoring')
    Start_ESC_Tx_monitoring.set('title', 'Initialize variables to start ESC Tx Monitoring')
    wait = etree.SubElement(Start_ESC_Tx_monitoring, "wait")
    wait.set('title', 'waiting variable set delay')
    wait.set('time', '500us')
    return

def Generate_decreasing_high_priority_bus_load_on_all_CAN_channels(local_Generate_decreasing_high_priority_bus_load_on_all_CAN_channels):
    print('Generate_decreasing_high_priority_bus_load_on_all_CAN_channels')
    Generate_decreasing_high_priority_bus_load_on_all_CAN_channels = etree.SubElement(testcase, "set")
    Generate_decreasing_high_priority_bus_load_on_all_CAN_channels.set('title', 'Decreasing bus load with high priority message on all CAN channels')
    sysvar = etree.SubElement(Generate_decreasing_high_priority_bus_load_on_all_CAN_channels, "sysvar")
    sysvar.set('name','HighBusLoadTestMode')
    sysvar.set('namespace','Ta')
    sysvar.text='10'
    return

def Stop_ESC_Tx_monitoring(local_Stop_ESC_Tx_monitoring):
    print('Stop_ESC_Tx_monitoring')
    Stop_ESC_Tx_monitoring = etree.SubElement(testcase, "capltestfunction")
    Stop_ESC_Tx_monitoring.set('name', 'StopEscTxMonitoring')
    Stop_ESC_Tx_monitoring.set('title', 'Reset variables to stop ESC Tx Monitoring')
    wait = etree.SubElement(Stop_ESC_Tx_monitoring, "wait")
    wait.set('title', 'waiting variable set delay')
    wait.set('time', '500us')
    return


def Check_value_HighBusLoadMaxPossible(local_Check_value_HighBusLoadMaxPossible):
    print('Check_value_HighBusLoadMaxPossible')
    local_Check_value_HighBusLoadMaxPossible1,local_Check_value_HighBusLoadMaxPossible2=local_Check_value_HighBusLoadMaxPossible.split(':')
    Check_value_HighBusLoadMaxPossible = etree.SubElement(testcase, "statecheck")
    Check_value_HighBusLoadMaxPossible.set('title', 'System/environment variable value check')
    Check_value_HighBusLoadMaxPossible.set('wait', '0')
    expected = etree.SubElement(Check_value_HighBusLoadMaxPossible, "expected")
    sysvar = etree.SubElement(expected, "sysvar")
    sysvar.set('name', 'HighBusLoadMaxPossible')
    sysvar.set('namespace', 'Ta')
    range = etree.SubElement(sysvar, "range")
    from1 = etree.SubElement(range, "from")
    from1.text=str(local_Check_value_HighBusLoadMaxPossible1)
    to = etree.SubElement(range, "to")
    to.text=str(local_Check_value_HighBusLoadMaxPossible2)
    return


def Message_Send(local_Message_Send):
    print('Message_Send')
    local_list_Message_Send=[]
    global comd_val
    local_Message_Send1,local_Message_Send2=local_Message_Send.split(':') #slipting message ID and data
    local_list_Message_Send=local_Message_Send2.split() #spliting message data based on space within data bytes and storing it inside list
    Message_Send = etree.SubElement(testcase, "set")
    Message_Send.set('title', 'Byte info')
    for Message_Send_i in range(0,len(local_list_Message_Send)):
        envvar = etree.SubElement(Message_Send, "envvar")
        envvar.set('name', 'Byte_'+str(Message_Send_i))
        envvar.text='0x'+str(local_list_Message_Send[Message_Send_i])

    Message_Send1 = etree.SubElement(testcase, "set")
    Message_Send1.set('title', 'Message_Send')
    envvar = etree.SubElement(Message_Send1, "envvar")
    envvar.set('name', 'Message_Send_'+local_Message_Send1)
    envvar.text='1'
    return

def Varset(local_Varset):
    global check_while_case_active
    global body
    print('Varset')
    if check_while_case_active==1:
        Varset = etree.SubElement(body, "varset_bycapl")
        Varset.set('name', 'loop_idx')
        caplparam = etree.SubElement(Varset, "caplparam")
        caplparam.set('name', 'loop_idx_t')
        caplparam.set('type', 'int')
        var = etree.SubElement(caplparam, "var")
        var.set('name', 'loop_idx')
        caplfunction = etree.SubElement(Varset, "caplfunction")

    return



def END_while_loop(local_END_while_loop):
   print('END_while_loop')
   global check_while_case_active
   check_while_case_active=0
   return




def check_symbol(local_check_symbol):
    print('check_symbol')
    symbol=['<','>','=','!=']
    for check_symbol_i in symbol:
        return check_symbol_i





def symbol_name():
    print('symbol_name')
    global value_val
    local_check_symbol=check_symbol(value_val)
    local_check_symbol_name=''
    if local_check_symbol=='<':
        local_check_symbol_name='lt'
    elif local_check_symbol=='>':
        local_check_symbol_name='gt'
    elif local_check_symbol=='=':
        local_check_symbol_name='eq'
    elif local_check_symbol=='!=':
        local_check_symbol_name='ne'
    else:
        local_check_symbol_name = 'not define'
    return local_check_symbol_name,local_check_symbol


def Start_while_loop(local_Start_while_loop):
    print('Start_while_loop')
    global body
    global check_while_case_active
    check_while_case_active=1
    start_local_check_symbol,local_check_symbol_name=symbol_name()
    Start_while_loop = etree.SubElement(testcase, "while_loop")
    Start_while_loop.set('title', 'while')
    condition = etree.SubElement(Start_while_loop, "condition")
    vareval = etree.SubElement(condition, "vareval")
    vareval.set('name','loop_idx')
    Start_while_loop_local1,Start_while_loop_local2=local_Start_while_loop.split(local_check_symbol_name)
    while_val = etree.SubElement(vareval, start_local_check_symbol)#while_val is coresponding to lt,ne,gt,ne
    while_val.text=str(Start_while_loop_local2)
    body = etree.SubElement(Start_while_loop, "body")
    wait = etree.SubElement(body, "wait")
    wait.set('title','Wait for 100ms')
    wait.set('time', '100ms')


    return

def if_case(local_if_case):
    print('if_case')
    #global value_val_next #not used
    #global comd_val_next #not used
    global value_val
    global body
    global check_while_case_active
    global if_case_check_active
    global if_body
    if_case_local_list=[]
    if_case_local_list1=[]
    if_case_check_active=1
    #local_if_case1, local_if_case2 = value_val.split('==')
    if_case_local_list=value_val.split('==')
    if_case_local_list1 = if_case_local_list[0].split('::')
    if(check_while_case_active==1):
        if(if_case_local_list1[0]=='sysvar'):

            if_case = etree.SubElement(body, "choice")
            if_case.set('title', 'if clause')
            if_ = etree.SubElement(if_case, "if")
            condition = etree.SubElement(if_, "condition")
            sysvar = etree.SubElement(condition, 'sysvar')
            sysvar.set('name', if_case_local_list1[2])
            sysvar.set('namespace', if_case_local_list1[1])
            sysvar.text = str(if_case_local_list[1])
            if_body = etree.SubElement(if_, "body")
            print('if_case_sysvar')

        elif(if_case_local_list1[0]=='envvar'):
            if (len(if_case_local_list1) == 3):

                if_case = etree.SubElement(body, "choice")
                if_case.set('title', 'if clause')
                if_ = etree.SubElement(if_case, "if")
                condition = etree.SubElement(if_, "condition")
                envvar = etree.SubElement(condition, 'envvar')
                envvar.set('name', if_case_local_list1[2] + if_case_local_list1[1])
                # sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                envvar.text = str(if_case_local_list[1])
                if_body = etree.SubElement(if_, "body")
                print('if_case_envvar3')
            elif (len(if_case_local_list1) == 2):

                if_case = etree.SubElement(body, "choice")
                if_case.set('title', 'if clause')
                if_ = etree.SubElement(if_case, "if")
                condition = etree.SubElement(if_, "condition")
                envvar = etree.SubElement(condition, 'envvar')
                envvar.set('name', if_case_local_list1[1] + if_case_local_list1[0])
                # sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                envvar.text = str(if_case_local_list[1])
                if_body = etree.SubElement(if_, "body")
                print('if_case_envvar2')
            else:
                pass
                print('check enviroment var')



        else:
            if_case = etree.SubElement(body, "choice")
            if_ = etree.SubElement(if_case, "if clause")
            condition = etree.SubElement(if_, "condition")
            cansignal = etree.SubElement(condition, "cansignal")
            cansignal.set('name', if_case_local_list[0])
            eq = etree.SubElement(cansignal, "eq")
            eq.text = str(if_case_local_list[1])
            if_body = etree.SubElement(if_case, "body")
            print('if_case_normal_var')

    else:
        if_case = etree.SubElement(testcase, "choice")
        if_ = etree.SubElement(if_case, "if clause")
        condition = etree.SubElement(if_, "condition")
        cansignal = etree.SubElement(condition, "cansignal")
        cansignal.set('name', if_case_local_list[0])
        eq = etree.SubElement(cansignal, "eq")
        eq.text=str(if_case_local_list[1])
        if_body = etree.SubElement(if_case, "body")
        print('if case not inside while')

    return

def Set(local_Set):
    print('Set')
    global if_case_check_active
    global if_body
    local_Set_list=[]
    local_Set_list1=[]
    #local_set1,local_set2=local_Set.split('=')
    local_Set_list=local_Set.split('=')
    #local_set3,local_set4,local_set5=local_set1.split("::")
    local_Set_list1=local_Set_list[0].split("::")
    if if_case_check_active==1:
        if(local_Set_list1[0]=='sysvar'):

            set = etree.SubElement(if_body, "set")
            set.set('title', 'set_sysvar_Enviroment')
            sysvar = etree.SubElement(set, 'sysvar')
            sysvar.set('name', local_Set_list1[2])
            sysvar.set('namespace', local_Set_list1[1])
            sysvar.text = str(local_Set_list[1])
            wait = etree.SubElement(if_body, "wait")
            wait.set('title', 'waiting variable set delay')
            wait.set('time', '500us')
            print('Set sysvar ')
        elif(local_Set_list1[0]=='envvar'):
            if(len(local_Set_list1)==3):

                set = etree.SubElement(if_body, "set")
                set.set('title', 'set_envvar_Enviroment')
                envvar = etree.SubElement(set, 'envvar')
                envvar.set('name', local_Set_list1[2]+local_Set_list1[1])
                #sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                envvar.text = str(local_Set_list[1])
                #wait = etree.SubElement(if_body, "wait")
                #wait.set('title', 'waiting variable set delay')
                #wait.set('time', '500us')
                print('Set envvar is 3')
            elif(len(local_Set_list1)==2):
                set = etree.SubElement(if_body, "set")
                set.set('title', 'set_envvar_Enviroment')
                envvar = etree.SubElement(set, 'envvar')
                envvar.set('name', local_Set_list1[2])
                #sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                envvar.text = str(local_Set_list[1])
                #wait = etree.SubElement(if_body, "wait")
                #wait.set('title', 'waiting variable set delay')
                #wait.set('time', '500us')
                print('Set envvar is 2')
            else:
                pass
                print('envvar is not correct')

        else:

            varset = etree.SubElement(if_body, "varset")
            varset.set('name', 'loop_idx')
            varset.text=str(local_Set_list[1])
            print('varset var set')

    else:
            # print('envar execute without if please check')
            # varset = etree.SubElement(testcase, "varset")
            # varset.set('name', 'loop_idx')
            # varset.text=str(local_Set_list[1])
            if (local_Set_list1[0] == 'sysvar'):
                set = etree.SubElement(testcase, "set")
                set.set('title', 'set_sysvar_Enviroment')
                sysvar = etree.SubElement(set, 'sysvar')
                sysvar.set('name', local_Set_list1[2])
                sysvar.set('namespace', local_Set_list1[1])
                sysvar.text = str(local_Set_list[1])
                wait = etree.SubElement(set, "wait")
                #wait.set('title', 'waiting variable set delay')
                #wait.set('time', '500us')
                print('Set sysvar ')
            elif (local_Set_list1[0] == 'envvar'):
                if (len(local_Set_list1) == 3):
                    set = etree.SubElement(testcase, "set")
                    set.set('title', 'set_envvar_Enviroment')
                    envvar = etree.SubElement(set, 'envvar')
                    envvar.set('name', local_Set_list1[2] + local_Set_list1[1])
                    # sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                    envvar.text = str(local_Set_list[1])
                    #wait = etree.SubElement(set, "wait")
                    #wait.set('title', 'waiting variable set delay')
                    #wait.set('time', '500us')
                    print('Set envvar is 3')
                elif (len(local_Set_list1) == 2):
                    set = etree.SubElement(testcase, "set")
                    set.set('title', 'set_envvar_Enviroment')
                    envvar = etree.SubElement(set, 'envvar')
                    envvar.set('name', local_Set_list1[1])
                    # sysvar.set('namespace', local_Set_list1[1]) no need of namespace in envvar
                    envvar.text = str(local_Set_list[1])
                    #wait = etree.SubElement(set, "wait")
                    #wait.set('title', 'waiting variable set delay')
                    #wait.set('time', '500us')
                    print('Set envvar is 2')
                else:
                    pass
                    print('envvar is not correct')


    return

def End_if_case(local_End_if_case):
    global if_case_check_active
    if_case_check_active=0
    return





#############################busOFF_BUSload condition########################################
def DLC(local_DLC):
    global value_val
    print('DLC')
    #local_DLC1, local_DLC2 = value_val.split('=')No need to varible value becouse it taook it from DLC

    DLC = etree.SubElement(testcase, "conditions")
    dlc_ok = etree.SubElement(DLC, "dlc_ok")
    dlc_ok.set('title', 'DLC Check')
    dlc_ok.set('dir', 'tx')
    canmsg = etree.SubElement(dlc_ok, "canmsg")
    canmsg.set('id',value_val)
    canmsg.set('bus','Main CAN')
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'Wait for 5s')
    wait.set('time', '5s')
    return


# def cycletime(local_cycletime): already function define above
#     global value_val
#     print('local_cycletime')
#     local_cycletime1, local_cycletime2 = value_val.split('=')
#     local_cycletime3, local_cycletime4 = local_cycletime2.split(':')
#     constraints = etree.SubElement(testcase, "constraints")
#     cycletime_abs = etree.SubElement(constraints, "cycletime_abs")
#     cycletime_abs.set('title', 'Cycle Time Check')
#     cycletime_abs.set('min', local_cycletime3)
#     cycletime_abs.set('max', local_cycletime4)
#     cycletime_abs.set('variants', "")
#
#
#     canmsg = etree.SubElement(cycletime_abs, "canmsg")
#     canmsg.set('id', local_cycletime1)
#     canmsg.set('bus', 'Main CAN')
#
#     wait = etree.SubElement(testcase, "wait")
#     wait.set('title', 'Wait for 5s')
#     wait.set('time', '5s')
#
#     return



def Short (local_Short):
    global value_val
    print('Short')
    local_Short1, local_Short2 = value_val.split(' and ')
    Short  = etree.SubElement(testcase, "capltestfunction")
    Short .set('title', 'Short' +local_Short1+ 'to' +local_Short2+ 'Recover')
    Short .set('name', 'Short_'+local_Short1+'to'+local_Short2+'_Func_MainCAN')
    return




def convert_dtc(local_convert_dtc):
    global DTC_value
    DTC_len=len(local_convert_dtc)
    if(local_convert_dtc[0]=='U'):
        local_convert_dtc=local_convert_dtc.replace('U','C0')

    local_convert_dtc = " ".join(local_convert_dtc[i:i + 2] for i in range(0, len(local_convert_dtc), 2))
    return(local_convert_dtc)

def FIT(local_FIT):
    global value_val
    print('FIT')
    local_FIT1, local_FIT2 = value_val.split('=')
    local_FIT3,local_FIT4=local_FIT1.split(':')
    FIT = etree.SubElement(testcase, "set")
    FIT.set('title', 'Fault injection trigger')
    envvar = etree.SubElement(FIT, "envvar")
    envvar.set('name', local_FIT4.strip()+'_'+local_FIT3.strip()+'_p1')
    envvar.text=str(local_FIT2)
    envvar = etree.SubElement(FIT, "envvar")
    envvar.set('name', local_FIT4.strip() + '_' + local_FIT3.strip()  + '_ih')
    envvar.text =str(0)
    envvar = etree.SubElement(FIT, "envvar")
    envvar.set('name', local_FIT4.strip()+ '_' + local_FIT3.strip()  + '_cp')
    envvar.text =str(0)
    envvar = etree.SubElement(FIT, "envvar")
    envvar.set('name', local_FIT4.strip() + '_' + local_FIT3.strip()  + '_fd')
    envvar.text =str(0)
    envvar = etree.SubElement(FIT, "envvar")
    envvar.set('name', local_FIT4.strip() + '_' + local_FIT3.strip()  + '_ft')
    envvar.text =str(1)
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set dealy')
    wait.set('time', '500us')
    return


def Recover_fault(local_Recover_fault):
    global value_val
    print('Recover_fault')
    local_Recover_fault1, local_Recover_fault2 = value_val.split(':')
    Recover_fault = etree.SubElement(testcase, "set")
    Recover_fault.set('title', 'Recover from signal fault')
    envvar = etree.SubElement(Recover_fault, "envvar")
    envvar.set('name', local_Recover_fault2+'_'+local_Recover_fault1+'_ft')
    envvar.text=str(0)
    return

def Check_FaultDetectTime(local_Check_FaultDetectTime):
    global value_val
    print('Check_FaultDetectTime')
    local_FaultDetectTime1, local_FaultDetectTime2 = value_val.split(':')
    Check_FaultDetectTime = etree.SubElement(testcase, "statecheck")
    Check_FaultDetectTime.set('title', 'Response time check')
    Check_FaultDetectTime.set('wait', '0')
    expected = etree.SubElement(Check_FaultDetectTime, "expected")
    sysvar = etree.SubElement(expected, "sysvar")
    sysvar.set('name', 'FaultDetectTime')
    sysvar.set('namespace', 'Ta')
    range = etree.SubElement(sysvar, "range")
    from1 = etree.SubElement(range, "from")
    from1.text=str(local_FaultDetectTime1)
    to = etree.SubElement(range, "to")
    to.text = str(local_FaultDetectTime2)

    return


def Trigger_Monitering(local_Trigger_Monitering):
    global value_val
    print('Trigger_Monitering')
    Trigger_Monitering = etree.SubElement(testcase, "set")
    Trigger_Monitering.set('title', 'Trigger flag log monitoring')
    sysvar = etree.SubElement(Trigger_Monitering, "sysvar")
    sysvar.set('name', 'FlagLogSig')
    sysvar.set('namespace', 'Ta')
    sysvar.text=str(value_val)+'_CAN_RxErrFlg'
    sysvar = etree.SubElement(Trigger_Monitering, "sysvar")
    sysvar.set('name', 'FlagLogSigTriggerV')
    sysvar.set('namespace', 'Ta')
    sysvar.text =str(1)
    sysvar = etree.SubElement(Trigger_Monitering, "sysvar")
    sysvar.set('name', 'FlagLogState')
    sysvar.set('namespace', 'Ta')
    sysvar.text = str(1)
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set dealy')
    wait.set('time', '500us')

    return

def Recover_Short(local_Recover_Short ):
    global value_val
    print('Recover_Short')
    local_Recover_Short1, local_Recover_Short2 = value_val.split('and')
    Recover_Short = etree.SubElement(testcase, "capltestfunction")
    Recover_Short.set('title', 'Short' +local_Recover_Short1+ 'to' +local_Recover_Short2+ 'Recover')
    Recover_Short.set('name', 'Recover_Short_'+local_Recover_Short1+'to'+local_Recover_Short2+'_Func_MainCAN')
    return



def Check_Tx_message_Shutdown_Time(local_Check_Tx_message_Shutdown_Time):

    global value_val
    print("Check_Tx_message_Shutdown_Time")
    local_Tx_message_Shutdown_Time1, local_Tx_message_Shutdown_Time2 = value_val.split('=')
    local_Tx_message_Shutdown_Time3,local_Tx_message_Shutdown_Time4=value_val.split(':')

    statecheck = etree.SubElement(testcase, "statecheck")#fixed
    statecheck.set('title', 'Shutdown delay time (until last Tx frame)')#fixed
    statecheck.set('wait', '0')#fixed
    expected = etree.SubElement(statecheck, "expected")#fixed
    sysvar = etree.SubElement(expected, "sysvar")#fixed
    sysvar.set('name', 'ShutdownTime')#fixed
    sysvar.set('namespace', 'Ta')#fixed
    range = etree.SubElement(sysvar, "range")#fixed
    from1 = etree.SubElement(range, "from")#fixed
    from1.text=str(0)#fixed
    to = etree.SubElement(range, "to")#fixed
    to.text=str(500)#fixed

    statecheck = etree.SubElement(testcase, "statecheck")  # fixed need to chech whicle execution if i need to use statecheck1 insted of statecheck as i used it earlier
    statecheck.set('title', 'Shutdown delay time (all listed Tx frame)')  # fixed
    statecheck.set('wait', '0')  # fixed
    expected = etree.SubElement(statecheck, "expected")  # fixed
    envvar = etree.SubElement(expected, "envvar")  # fixed
    envvar.set('name','Env_'+local_Tx_message_Shutdown_Time1+'_SdnDelayTime')  # varible
    range = etree.SubElement(envvar, "range")  # fixed
    from1 = etree.SubElement(range, "from")#fixed
    from1.text=str(local_Tx_message_Shutdown_Time3)#fixed
    to = etree.SubElement(range, "to")#fixed
    to.text=str(local_Tx_message_Shutdown_Time4)#fixed
    return






def Check_Tx_message_Startup_Time(local_Check_Tx_message_Startup_Time):
    global value_val
    print("Check_Tx_message_Startup_Time")
    local_Tx_message_Startup_Time1, local_Tx_message_Startup_Time2 = value_val.split('=')
    local_Tx_message_Startup_Time3,local_Tx_message_Startup_Time4=local_Tx_message_Startup_Time2.split(':')

    statecheck = etree.SubElement(testcase, "statecheck")#fixed
    statecheck.set('title', 'Wake-up time (until first Tx frame)')#fixed
    statecheck.set('wait', '0')#fixed
    expected = etree.SubElement(statecheck, "expected")#fixed
    sysvar = etree.SubElement(expected, "sysvar")#fixed
    sysvar.set('name', 'WakeUpTime')#fixed
    sysvar.set('namespace', 'Ta')#fixed
    range = etree.SubElement(sysvar, "range")#fixed
    from1 = etree.SubElement(range, "from")#fixed
    to = etree.SubElement(range, "to")#fixed
    from1.text = str(0)  # fixed
    to.text=str(500)#fixed

    statecheck = etree.SubElement(testcase, "statecheck")  # fixed need to chech whicle execution if i need to use statecheck1 insted of statecheck as i used it earlier
    statecheck.set('title', 'Wake-up time (all listed Tx frame)')  # fixed
    statecheck.set('wait', '0')  # fixed
    expected = etree.SubElement(statecheck, "expected")  # fixed
    envvar = etree.SubElement(expected, "envvar")  # fixed
    envvar.set('name','Env_'+local_Tx_message_Startup_Time1+'_WUpDelayTime')  # varible
    range = etree.SubElement(envvar, "range")  # fixed
    from1 = etree.SubElement(range, "from")#fixed
    from1.text=str(local_Tx_message_Startup_Time3)#fixed
    to = etree.SubElement(range, "to")#fixed
    to.text=str(local_Tx_message_Startup_Time4)#fixed
    return



def Trigger_shutdown_time(local_Trigger_shutdown_time):
    Trigger_shutdown_time = etree.SubElement(testcase, "capltestfunction")
    Trigger_shutdown_time.set('title', 'Trigger shutdown time measurement')
    Trigger_shutdown_time.set('name', 'ReadyForShutdownMeasurement')
    return

def Trigger_wake_up_time(local_Trigger_wake_up_time):
    Trigger_wake_up_time = etree.SubElement(testcase, "capltestfunction")
    Trigger_wake_up_time.set('title', 'Trigger wake-up time measurement')
    Trigger_wake_up_time.set('name', 'ReadyForWakeUpMeasurement')
    return

###############oldv1.0#######################
def completion_func():
    completion = etree.SubElement(root, "completion")
    capltestfunction = etree.SubElement(completion, "capltestfunction")
    capltestfunction.set('title', 'test completion')
    capltestfunction.set('name', 'TestGroupCompletion')
    print("completion")
    return



def Set_Timeout(local_Set_Timeout):
    print("Set_Timeout")

    set = etree.SubElement(testcase, "set")
    set.set('title', 'set fault info')
    envvar = etree.SubElement(set, "envvar")
    envvar.set('name','Env_'+value_val+'_Timeout')
    envvar.text=str(1)
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set dealy')
    wait.set('time', "500us")
    return

def Power_supply(local_power_supply_val):
    global value_val
    print("local_power_supply_val")
    set = etree.SubElement(testcase, "set")
    set.set('title', 'Set Voltage')
    envvar = etree.SubElement(set, "envvar")
    envvar.set('name', 'Set_Voltage')
    local_value_val=str(value_val)
    envvar.text=str(value_val[:-1])
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'Power supply')
    capltestfunction.set('name', "PowerSupplyChange")
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting')
    wait.set('time', "1ms")

    return

def Initialize_CAN_Interface(local_Initialize_CAN_Interface_val):
    print("Initialize_CAN_Interface")
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'Initialize_CAN_Interface_val')
    capltestfunction.set('name', "InitAllVar")
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting')
    wait.set('time', "1ms")
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'Release init state')
    capltestfunction.set('name', "ReleaseInitVarState")
    return

def Wait(local_wait_val):
    global value_val
    global check_for_loop_start_active
    global for_loop_start
    if check_for_loop_start_active==1:
        wait = etree.SubElement(for_loop_start, "wait")
        wait.set('title', 'waiting')
        wait.set('time', value_val)
        print("Wait for for loop")
    else:
        wait = etree.SubElement(testcase, "wait")
        wait.set('title', 'waiting')
        wait.set('time', value_val)
        print('wait')
    return
def Operation(local_operation_val):
    print("local_operation_val")
    return

def DTC_Check(local_DTC_Read):
    global DTC_value
    print("DTC_Check")
    varset = etree.SubElement(testcase, "varset")
    varset.set('name', "BufferDTCList")
    varset.text='NA'
    diagservice = etree.SubElement(testcase, "diagservice")
    diagservice.set('title', "Check DTC")
    diagservice.set('ecu', "EPS_M8X")
    diagservice.set('reportservicedetails', "always")
    diagservice.set('service', "FaultMemory_Read_identified_errors")
    diagrequest = etree.SubElement(diagservice, "diagrequest")
    diagparam = etree.SubElement(diagrequest, "diagparam")
    diagparam.set('qualifier', "DtcStatusbyte")
    diagparam.text='0xff'
    diagresponse = etree.SubElement(diagservice, "diagresponse")
    diagparam = etree.SubElement(diagresponse, "diagparam")
    diagparam.set('qualifier', "ListOfDTCAndStatus")
    diagparam.set('format', "bytesequence")
    diagparam.set('copytovar', "BufferDTCList")
    ne = etree.SubElement(diagparam, "ne")
    ne.text='99'
    set = etree.SubElement(testcase, "set")
    set.set('title', "Copy DTC List to system variable")
    sysvar = etree.SubElement(set, "sysvar")
    sysvar.set('name', "DTCList")
    sysvar.set('namespace', "Ta")
    var = etree.SubElement(sysvar, "var")
    var.set('name', "BufferDTCList")
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set dealy')
    wait.set('time', '500us')
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'Compare DTC:')
    capltestfunction.set('name', 'CompareDTCList')
    caplparam = etree.SubElement(capltestfunction, "caplparam")
    caplparam.set('name', 'expDTC')
    caplparam.set('type', 'string')
    if(DTC_value!=''):
        local_DTC_value=convert_dtc(str(DTC_value))
        caplparam.text=str(local_DTC_value)
    else:
        pass
    return



def Check_variable(local_check_variable):
    global value_val
    print("check_variable")
    check_varible1,local_check_variable2=value_val.split('=')
    statecheck = etree.SubElement(testcase, "statecheck")
    statecheck.set('title', "Check "+check_varible1)
    statecheck.set('wait', '0')
    expected = etree.SubElement(statecheck, "expected")
    cansignal = etree.SubElement(expected, "cansignal")
    cansignal.set('name', check_varible1)
    cansignal.set('msg', 'EPS_ALIVE_CHKSM')
    cansignal.set('bus', 'Main CAN')
    #cansignal.set('variants', varient_list[main_func_j])#varient name from global list
    cansignal.text=str(local_check_variable2)

    return

def Recover_timeout(local_Recover_timeout):
    print("Recover_timeout")
    set = etree.SubElement(testcase, "set")
    set.set('title', 'Recover_timeout_info')
    envvar = etree.SubElement(set, "envvar")
    envvar.set('name','Env_'+value_val+'_Timeout')
    envvar.text=str(0)
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting variable set dealy')
    wait.set('time', "500us")
    return

def DTC_Clear(local_DTC_Clear):
    print("DTC_Clear")
    diagservice = etree.SubElement(testcase, "diagservice")
    diagservice.set('title', 'Clear DTC')
    diagservice.set('ecu', 'EPS_M8X')
    diagservice.set('service', 'FaultMemory_Clear_all_errors')
    diagrequest = etree.SubElement(diagservice, "diagrequest")
    diagparam = etree.SubElement(diagrequest, "diagparam")
    diagparam.set('qualifier', 'GroupOfDtc')
    diagparam.text="All groups"
    diagresponse = etree.SubElement(diagservice, "diagresponse")
    return

def IGN_OFF(local_IGN_OFF):
    print("IGN_OFF")
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'IGN_OFF')
    capltestfunction.set('name', "StateSignal_IGN_OFF")
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting')
    wait.set('time', "1ms")
    return

def IGN_ON(local_IGN_ON):
    print("IGN_ON")
    capltestfunction = etree.SubElement(testcase, "capltestfunction")
    capltestfunction.set('title', 'IGN_ON')
    capltestfunction.set('name', "StateSignal_IGN_ON")
    wait = etree.SubElement(testcase, "wait")
    wait.set('title', 'waiting')
    wait.set('time', "1ms")
    return



dict1={'Initialize CAN Interface':Initialize_CAN_Interface,'Wait':Wait,'Operation':Operation,'Power_supply':Power_supply,'Set_Timeout':Set_Timeout,'DTC_Check':DTC_Check,'Check_CAN_variable':Check_variable,'Recover_timeout':Recover_timeout,'DTC_Clear':DTC_Clear,'IGN_OFF':IGN_OFF, \
       'IGN_ON':IGN_ON,'Trigger_wake_up_time':Trigger_wake_up_time,'Trigger_shutdown_time':Trigger_shutdown_time,'Check_Tx_message_Startup_Time':Check_Tx_message_Startup_Time,'Check_Tx_message_Shutdown_Time':Check_Tx_message_Shutdown_Time,'Trigger_Monitering':Trigger_Monitering, \
       'Check_FaultDetectTime':Check_FaultDetectTime,'Recover_fault':Recover_fault,'FIT':FIT,'convert_dtc':convert_dtc,'Short':Short,'cycletime':cycletime,'DLC':DLC,'Recover_Short':Recover_Short,'Start_while_loop':Start_while_loop,\
       'if_case':if_case,'END_while_loop':END_while_loop,'Set':Set,'End_if_case':End_if_case,'Message_Send':Message_Send,'Check_value_HighBusLoadMaxPossible':Check_value_HighBusLoadMaxPossible,'Stop_ESC_Tx_monitoring':Stop_ESC_Tx_monitoring,'Generate_decreasing_high_priority_bus_load_on_all_CAN_channels':Generate_decreasing_high_priority_bus_load_on_all_CAN_channels,\
       'Start_ESC_Tx_monitoring':Start_ESC_Tx_monitoring,'Stop_generating_bus_load_test_message':Stop_generating_bus_load_test_message,'Generate_increasing_high_priority_bus_load_on_all_CAN_channels':Generate_increasing_high_priority_bus_load_on_all_CAN_channels,'Message_Stop':Message_Stop,\
       'DLC_check_stop':DLC_check_stop,'DLC_check':DLC_check,'DLC_check_start':DLC_check_start,'for_loop_stop':for_loop_stop,'Check_signal':Check_signal,'for_loop_start':for_loop_start,'Varset':Varset,'Check_value':Check_value,'constraints_start':constraints_start,'constraints_stop':constraints_stop,\
       'Power_supply_OFF':Power_supply_OFF,'Power_supply_ON':Power_supply_ON,'Range_check':Range_check,'IGN_OFF_Wakeup':IGN_OFF_Wakeup,'IGN_ON_Wakeup':IGN_ON_Wakeup,'IGN_ON_ShutDown':IGN_ON_ShutDown,'IGN_OFF_ShutDown':IGN_OFF_ShutDown} #dictionary for generating switch case



def genrate_func(local_cmd,local_val):

    dict1[local_cmd](local_val)#use to access dictionary value
    return



def sub_engine(sub_engine1,sun_engine2):
    global my_try_list_cmd
    global my_try_list_data
    global global_j
    global comd_val
    global value_val
    global testcase
    global DTC_value
    for local_sub_engine_i in range(sub_engine1+1,sun_engine2):
        check_test_case_local=sheet['B' + str(local_sub_engine_i)].value

        if(check_test_case_local=='Test case'):
            DTC_value = sheet['P' + str(local_sub_engine_i)].value #Update DTC based on Test case
            testcase = etree.SubElement(testgroup, "testcase")
            testcase.set('title', sheet['I' + str(local_sub_engine_i)].value)
            testcase.set('ident', sheet['D' + str(local_sub_engine_i)].value)
            testcase.set('variants', sheet['J' + str(local_sub_engine_i)].value)

            description = etree.SubElement(testcase, "description")
            description.text = sheet['I' + str(local_sub_engine_i)].value

            preparation = etree.SubElement(testcase, "preparation")
            capltestfunction = etree.SubElement(preparation, "capltestfunction")
            capltestfunction.set('title', "Change logging file name")
            capltestfunction.set('name', "LogFileChangeTrigger")

            caplparam = etree.SubElement(capltestfunction, "caplparam")
            caplparam.set('name', "fname")
            caplparam.set('type', "string")
            caplparam.text = (sheet['D' + str(local_sub_engine_i)].value)


        comd_val=sheet['AK' + str(local_sub_engine_i)].value
        value_val=sheet['AL' + str(local_sub_engine_i)].value
        if value_val!=None:
            value_val=value_val.strip()#for removing spacing from varible if any
        if comd_val != None:
            comd_val = comd_val.strip()  # for removing spacing from varible if any



        my_try_list_cmd[global_j].append(comd_val)#Not using my_try_list_cmd
        my_try_list_data[global_j].append(value_val)#Not using my_try_list_data
        genrate_func(comd_val, str(value_val))
    #local_j=global_j+1 #for increment list dimention by 1
    #print(my_try_list_cmd)
    #print(my_try_list_data)

    return




def Main_Engine(main_arg1,main_arg2):
    global wb
    global sheet
    global testgroup
    global testcase
    global description
    global preparation
    global DTC_value
    testgroup = etree.SubElement(root, "testgroup")
    testgroup.set('title',sheet['I' + str(main_arg1)].value)
   # DTC_value = sheet['P' + str(main_arg1 + 1)].value removing DTC based on heading
    sub_engine(main_arg1,main_arg2) # to get and generated diff functions
    return

def readxls_file():
    global faltu_list
    global wb
    global sheet
    readxls_file_i=1

    faltu_list.append((sheet['I' + '3'].value))
    faltu_list.append((sheet['I' + '4'].value))
    local_readxlx_val=(sheet['B' + str(readxls_file_i)].value)
    while(local_readxlx_val!='END'): #this section will find END variable to find total length of test cases.
        local_readxlx_val = sheet['B' + str(readxls_file_i)].value
        readxls_file_i+=1

    for i in range(6, readxls_file_i):
        local_check=(sheet['B' + str(i)].value)
        if(local_check)=="Heading" or local_check=="END":
            Testtcase_list.append(i)
        if(local_check)=="Test case":
            varient_list.append((sheet['J' + str(i)].value))

    print(Testtcase_list)
    print(varient_list)
    return



def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

    return



readxls_file()


root=Element('testmodule')
tree=ElementTree(root)
root.set('title',faltu_list[0])
root.set('version',faltu_list[1])
root.set('xmlns','http://www.vector-informatik.de/CANoe/TestModule/1.25')



variants = etree.SubElement(root, "variants")

removed_duplicacy_list=list(set(varient_list))#removed duplicacy in varient data.
for local_variant_i in range(0,len(removed_duplicacy_list)):#set varient_list -1 to remove last 'none' varient from varient list
    variant = etree.SubElement(variants, "variant")
  #  local_variant_1 = etree.SubElement(variants, "variant")
    variant.set('name', str(removed_duplicacy_list[local_variant_i]))
    global_local_variant_i=local_variant_i #for getting varient index at global level
   # local_variant_1.set('name', str(varient_list[1]))

preparation = etree.SubElement(root, "preparation")
vardef = etree.SubElement(preparation, "vardef")
vardef.set('name','BufferDTCList')
vardef.set('type','string')
vardef.text='NotAssigned'
vardef = etree.SubElement(preparation, "vardef")
vardef.set('name','BufferDTCStatusList')
vardef.set('type','string')
vardef.text='NotAssigned'
vardef = etree.SubElement(preparation, "vardef")
vardef.set('name','loop_idx')
vardef.set('type','int')
vardef.text='0'



#############main functionality start here

for main_func_i in range(1,len(Testtcase_list)):

    Main_Engine(Testtcase_list[main_func_j],Testtcase_list[main_func_j+1]) #main engine function call depend on the no oftest case.
    my_try_list_cmd = my_try_list_cmd + [[]] #not using 2d list
    my_try_list_data=my_try_list_data+[[]] #not using 2d list
    main_func_j=main_func_j+1





completion_func()
indent(root)
tree.write("Comm_automation.xml", encoding="iso-8859-1", xml_declaration=True)


























