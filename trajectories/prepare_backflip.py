import pandas as pd
import numpy as np

csv = pd.read_csv("./backflip/2023_12_07/trajectories/planarProblemBackflip.csv")
# load contact data
contact = np.load("./backflip/2023_12_07/trajectories/results.pkl", allow_pickle=True)["contactPhases"]
print(contact)
cp = np.zeros(len(csv),dtype=np.int8)
for c in contact:
    if c[0] == "none":
        if c[1].stop >= 0:
            cp[c[1]] = 0
        else:
            cp[c[1].start:] = 0
    elif c[0] == "single":
        if c[1].stop >= 0:
            cp[c[1]] = 1
        else:
            cp[c[1].start:] = 1
    elif c[0] == "dual":
        if c[1].stop >= 0:
            cp[c[1]] = 2
        else:
            cp[c[1].start:] = 2
d = {
    "t[s]": csv["time"],
    "q_fl1": np.zeros(len(csv)),
    "q_fl2": csv["back_hip_pos"],
    "q_fl3": csv["back_knee_pos"],
    "q_fr1": np.zeros(len(csv)),
    "q_fr2": csv["back_hip_pos"],
    "q_fr3": csv["back_knee_pos"],
    "q_bl1": np.zeros(len(csv)),
    "q_bl2": csv["front_hip_pos"],
    "q_bl3": csv["front_knee_pos"],
    "q_br1": np.zeros(len(csv)),
    "q_br2": csv["front_hip_pos"],
    "q_br3": csv["front_knee_pos"],
    "qd_fl1": np.zeros(len(csv)),
    "qd_fl2": csv["back_hip_vel"],
    "qd_fl3": csv["back_knee_vel"],
    "qd_fr1": np.zeros(len(csv)),
    "qd_fr2": csv["back_hip_vel"],
    "qd_fr3": csv["back_knee_vel"],
    "qd_bl1": np.zeros(len(csv)),
    "qd_bl2": csv["front_hip_vel"],
    "qd_bl3": csv["front_knee_vel"],
    "qd_br1": np.zeros(len(csv)),
    "qd_br2": csv["front_hip_vel"],
    "qd_br3": csv["front_knee_vel"],
    "Tau_fl1": np.zeros(len(csv)),
    "Tau_fl2": csv["back_hip_torque"]/2,
    "Tau_fl3": csv["back_knee_torque"]/2,
    "Tau_fr1": np.zeros(len(csv)),
    "Tau_fr2": csv["back_hip_torque"]/2,
    "Tau_fr3": csv["back_knee_torque"]/2,
    "Tau_bl1": np.zeros(len(csv)),
    "Tau_bl2": csv["front_hip_torque"]/2,
    "Tau_bl3": csv["front_knee_torque"]/2,
    "Tau_br1": np.zeros(len(csv)),
    "Tau_br2": csv["front_hip_torque"]/2,
    "Tau_br3": csv["front_knee_torque"]/2,
    "contactPhases": cp,
    }

df_control = pd.DataFrame(d)


# frame_correction
df_control['q_fl2'] = df_control['q_fl2'].apply(lambda x: x*-1)
df_control['q_fl3'] = df_control['q_fl3'].apply(lambda x: x*-1)
df_control['q_fr2'] = df_control['q_fr2'].apply(lambda x: x*-1)
df_control['q_fr3'] = df_control['q_fr3'].apply(lambda x: x*-1)
df_control['q_bl1'] = df_control['q_bl1'].apply(lambda x: x*-1)
df_control['q_br1'] = df_control['q_br1'].apply(lambda x: x*-1)

df_control['qd_fl2'] = df_control['qd_fl2'].apply(lambda x: x*-1)
df_control['qd_fl3'] = df_control['qd_fl3'].apply(lambda x: x*-1)
df_control['qd_fr2'] = df_control['qd_fr2'].apply(lambda x: x*-1)
df_control['qd_fr3'] = df_control['qd_fr3'].apply(lambda x: x*-1)
df_control['qd_bl1'] = df_control['qd_bl1'].apply(lambda x: x*-1)
df_control['qd_br1'] = df_control['qd_br1'].apply(lambda x: x*-1)

df_control['Tau_fl2'] = df_control['Tau_fl2'].apply(lambda x: x*-1)
df_control['Tau_fl3'] = df_control['Tau_fl3'].apply(lambda x: x*-1)
df_control['Tau_fr2'] = df_control['Tau_fr2'].apply(lambda x: x*-1)
df_control['Tau_fr3'] = df_control['Tau_fr3'].apply(lambda x: x*-1)
df_control['Tau_bl1'] = df_control['Tau_bl1'].apply(lambda x: x*-1)
df_control['Tau_br1'] = df_control['Tau_br1'].apply(lambda x: x*-1)

print(df_control)
df_control.to_csv("backflip231207_contact_frameCorrected.csv")
