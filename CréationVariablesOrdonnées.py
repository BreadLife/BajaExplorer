import random

MAX_RPM_AVG = 1000
MAX_RPM_AVD = 1000
MAX_RPM_ARR = 1000
MAX_TEMP_CVT = 100
MAX_RPM_MOT = 5000
MAX_TROT_POS = 100
MAX_SHV_POS = 360

rpm_av_d = random.randint(0,MAX_RPM_AVD)
rpm_av_g = random.randint(0,MAX_RPM_AVG)
rpm_arr = random.randint(0,MAX_RPM_ARR)
temp_cvt = random.randint(0,MAX_TEMP_CVT)
rpm_mot = random.randint(0,MAX_RPM_MOT)
throt_pos = random.randint(0,MAX_TROT_POS)
shv_pos = random.randint(0,MAX_SHV_POS)

rpm_av_d_sens = 0
rpm_av_g_sens = 0
rpm_arr_sens = 0
temp_cvt_sens = 0
rpm_mot_sens = 0
throt_pos_sens = 0
shv_pos_sens = 0

"""    #rpm
    if (rpm_av_d >= MAX_RPM_AVD and rpm_av_d_sens==1):
        rpm_av_d_sens = 0
    elif(rpm_av_d <= 0 and rpm_av_d_sens==0):
        rpm_av_d_sens = 1
    elif(rpm_av_d <= MAX_RPM_AVD and rpm_av_d_sens==1):
        rpm_av_d+=1
    elif (rpm_av_d >= MAX_RPM_AVD and rpm_av_d_sens==0):
        rpm_av_d+=1
"""

def Creation_Variables():
    rpm_av_d = random.randint(0, MAX_RPM_AVD)
    rpm_av_g = random.randint(0, MAX_RPM_AVG)
    rpm_arr = random.randint(0, MAX_RPM_ARR)
    temp_cvt = random.randint(0, MAX_TEMP_CVT)
    rpm_mot = random.randint(0, MAX_RPM_MOT)
    throt_pos = random.randint(0, MAX_TROT_POS)
    shv_pos = random.randint(0, MAX_SHV_POS)

    return rpm_av_d, rpm_av_g, rpm_arr, temp_cvt, rpm_mot, throt_pos, shv_pos