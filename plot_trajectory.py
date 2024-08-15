import pandas
from plotnine import ggplot, aes, geom_line, theme_bw, facet_grid, facet_wrap


def main():
    csv = pandas.read_csv("./trajectories/backflip_contact_frameCorrected_interp.csv")
    # csv = pandas.read_csv("./trajectories/planarProblemBackflip_23012023_frameCorrected_interp.csv")
    fl = pandas.melt(csv,id_vars=["t[s]"],value_vars=["q_fl1","q_fl2", "q_fl3","qd_fl1","qd_fl2", "qd_fl3","Tau_fl1","Tau_fl2", "Tau_fl3"], value_name="value", var_name="type")
    fr = pandas.melt(csv,id_vars=["t[s]"],value_vars=["q_fr1","q_fr2", "q_fr3","qd_fr1","qd_fr2", "qd_fr3","Tau_fr1","Tau_fr2", "Tau_fr3"], value_name="value", var_name="type")
    bl = pandas.melt(csv,id_vars=["t[s]"],value_vars=["q_bl1","q_bl2", "q_bl3","qd_bl1","qd_bl2", "qd_bl3","Tau_bl1","Tau_bl2", "Tau_bl3"], value_name="value", var_name="type")
    br = pandas.melt(csv,id_vars=["t[s]"],value_vars=["q_br1","q_br2", "q_br3","qd_br1","qd_br2", "qd_br3","Tau_br1","Tau_br2", "Tau_br3"], value_name="value", var_name="type")
    (
        ggplot(bl)
        + aes(x="t[s]", y="value", color="type")
        + geom_line()
        + theme_bw()
        + facet_wrap("~type",scales="free_y")
    ).draw(1)

    (
        ggplot(csv)
        + geom_line(aes("t[s]","contactPhase"))
        + theme_bw()
        
    ).draw(1)

if __name__ == "__main__":
    main()