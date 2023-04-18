from scipy import constants

# physical quantities
UNIT_CHARGE = 1.60217648700000E-19  # [C]
VAC_PERMITTIVITY = 8.85418781762039E-12  # [F/m]

# Atomic mass unit [kg]
AMU = 1.66053878200000E-27
# Avogadro const
NA = 6.02214076E+23

# AU
AU_TO_ANG = 5.29177208590000E-01
AU_TO_EV = 2.72113838565563E+01
AU_TO_EV_EVERY_ANG = AU_TO_EV / AU_TO_ANG
# [a.u.] = hbar / EHartree -> [s]
AU_2_S = 2.41888432650478E-17
# Angstrom to m
ANG_TO_M = 1E-10
ANG_TO_CM = 1E-08
PS_2_S = 1E-12
# epsilon [e/(V Angstrom)]
EPSILON = constants.epsilon_0 / constants.elementary_charge * constants.angstrom

DEBYE_TO_EA = 1. / 4.8
