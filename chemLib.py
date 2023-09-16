import re

# Ideal gas constant
Ratm = 0.0821
Rtorr = 62.4

def main():
    test_string = "H2O(Si(OH2)3)4"
    print(molar_mass(test_string))

class Elm:
    def __init__(self, num: int, m: float, name: str, 
                 period: int, group=None, group_long=None):
        self.num = num
        self.m = m
        self.name = name
        self.period = period
        self.group = group
        if group:
            self.group = int(group)
        self.group_long = group_long

    def print_info_line(self, criteria, datum, left_side_chars=16):
        print(f"{(left_side_chars - len(criteria) - 1) * ' '}{criteria}: {datum}")
    
    def show_info(self):
        info_dict = {
            "Name": self.name,
            "Atomic Number": self.num,
            "Atomic Mass": self.m,
            "Group": self.group,
            "Group_Long": self.group_long,
            "Period": self.period
        }
        for key, value in info_dict.items():
            if value:
                self.print_info_line(key, value)


def molar_mass(compound_string: str, sig_figs=False):
    """Calculate the molar mass of a compound
    
    Parameters
    ----------
    compound_string : str
        A string showing the compound for 
        which you want to calculate the mass
    sig_figs : bool
        Determine whether you want to round the 
        molar mass to the appropriate number of 
        significant figures
    
    Returns
    -------
    molar_mass : float
        The molar mass of the compound"""


    # First check if the number of open parentheses is the 
    # same as close parentheses
    if compound_string.count('(') != compound_string.count(')'):
        print("Opening and closing parentheses don't match, check your string")
        return
    mass = 0
    result = ""
    min_decimals = 8
    while result != None:
        atom_pat = r"[A-Z][a-z]?|\("
        result = re.search(atom_pat, compound_string)
        if result == None:
            break
        result = result.group()
        if result == '(':
            small_formula = re.search(r"(?<=\().*(?=\))", compound_string).group()
            item_mass = molar_mass(small_formula)
            compound_string = compound_string.split(small_formula + ")", maxsplit=1)[1]

        else:
            item_mass = eval(result + ".m")
            compound_string = re.split(atom_pat, compound_string, maxsplit=1)[1]
        multiplier_string = re.search(r"^\d+", compound_string)
        if multiplier_string == None:
            multiplier = 1
        else:
            multiplier = int(multiplier_string.group())
        min_decimals = len(str(item_mass).split('.')[1])
        mass += item_mass * multiplier
    return round(mass, 8)

H = Elm(1, 1.00794, "Hydrogen", 1, 1.0, "I A")
He = Elm(2, 4.002602, "Helium", 1, 18.0, "VIII A")

Li = Elm(3, 6.941, "Lithium", 2, 1.0, "I A")
Be = Elm(4, 9.012182, "Beryllium", 2, 2.0, "II A")
B = Elm(5, 10.811, "Boron", 2, 13.0, "III A")
C = Elm(6, 12.0107, "Carbon", 2, 14.0, "IV A")
N = Elm(7, 14.0067, "Nitrogen", 2, 15.0, "V A")
O = Elm(8, 15.9994, "Oxygen", 2, 16.0, "VI A")
F = Elm(9, 18.9984032, "Fluorine", 2, 17.0, "VII A")
Ne = Elm(10, 20.1797, "Neon", 2, 18.0, "VIII A")

Na = Elm(11, 22.98976928, "Sodium  (Natrium)", 3, 1.0, "I A")
Mg = Elm(12, 24.305, "Magnesium", 3, 2.0, "II A")
Al = Elm(13, 26.9815386, "Aluminium  (Aluminum)", 3, 13.0, "III A")
Si = Elm(14, 28.0855, "Silicon", 3, 14.0, "IV A")
P = Elm(15, 30.973762, "Phosphorus", 3, 15.0, "V A")
S = Elm(16, 32.065, "Sulfur", 3, 16.0, "VI A")
Cl = Elm(17, 35.453, "Chlorine", 3, 17.0, "VII A")
K = Elm(19, 39.0983, "Potassium  (Kalium)", 4, 1.0, "I A")
Ar = Elm(18, 39.948, "Argon", 3, 18.0, "VIII A")

Ca = Elm(20, 40.078, "Calcium", 4, 2.0, "II A")
Sc = Elm(21, 44.955912, "Scandium", 4, 3.0, "III B")
Ti = Elm(22, 47.867, "Titanium", 4, 4.0, "IV B")
V = Elm(23, 50.9415, "Vanadium", 4, 5.0, "V B")
Cr = Elm(24, 51.9961, "Chromium", 4, 6.0, "VI B")
Mn = Elm(25, 54.938045, "Manganese", 4, 7.0, "VII B")
Fe = Elm(26, 55.845, "Iron  (Ferrum)", 4, 8.0, "VIII B")
Co = Elm(27, 58.933195, "Cobalt", 4, 9.0, "VIII B")
Ni = Elm(28, 58.6934, "Nickel", 4, 10.0, "VIII B")
Cu = Elm(29, 63.546, "Copper  (Cuprum)", 4, 11.0, "I B")
Zn = Elm(30, 65.409, "Zinc", 4, 12.0, "II B")
Ga = Elm(31, 69.723, "Gallium", 4, 13.0, "III A")
Ge = Elm(32, 72.64, "Germanium", 4, 14.0, "IV A")
As = Elm(33, 74.9216, "Arsenic", 4, 15.0, "V A")
Se = Elm(34, 78.96, "Selenium", 4, 16.0, "VI A")
Br = Elm(35, 79.904, "Bromine", 4, 17.0, "VII A")
Kr = Elm(36, 83.798, "Krypton", 4, 18.0, "VIII A")

Rb = Elm(37, 85.4678, "Rubidium", 5, 1.0, "I A")
Sr = Elm(38, 87.62, "Strontium", 5, 2.0, "II A")
Y = Elm(39, 88.90585, "Yttrium", 5, 3.0, "III B")
Zr = Elm(40, 91.224, "Zirconium", 5, 4.0, "IV B")
Nb = Elm(41, 92.906, "Niobium", 5, 5.0, "V B")
Mo = Elm(42, 95.94, "Molybdenum", 5, 6.0, "VI B")
Tc = Elm(43, 98.0, "Technetium", 5, 7.0, "VII B")
Ru = Elm(44, 101.07, "Ruthenium", 5, 8.0, "VIII B")
Rh = Elm(45, 102.905, "Rhodium", 5, 9.0, "VIII B")
Pd = Elm(46, 106.42, "Palladium", 5, 10.0, "VIII B")
Ag = Elm(47, 107.8682, "Silver  (Argentum)", 5, 11.0, "I B")
Cd = Elm(48, 112.411, "Cadmium", 5, 12.0, "II B")
In = Elm(49, 114.818, "Indium", 5, 13.0, "III A")
Sn = Elm(50, 118.71, "Tin  (Stannum)", 5, 14.0, "IV A")
Sb = Elm(51, 121.76, "Antimony  (Stibium)", 5, 15.0, "V A")
Te = Elm(52, 127.6, "Tellurium", 5, 16.0, "VI A")
I = Elm(53, 126.904, "Iodine", 5, 17.0, "VII A")
Xe = Elm(54, 131.293, "Xenon", 5, 18.0, "VIII A")

Cs = Elm(55, 132.9054519, "Caesium  (Cesium)", 6, 1.0, "I A")
Ba = Elm(56, 137.327, "Barium", 6, 2.0, "II A")
La = Elm(57, 138.90547, "Lanthanum", 6)
Ce = Elm(58, 140.116, "Cerium", 6)
Pr = Elm(59, 140.90765, "Praseodymium", 6)
Nd = Elm(60, 144.242, "Neodymium", 6)
Pm = Elm(61, 145.0, "Promethium", 6)
Sm = Elm(62, 150.36, "Samarium", 6)
Eu = Elm(63, 151.964, "Europium", 6)
Gd = Elm(64, 157.25, "Gadolinium", 6)
Tb = Elm(65, 158.92535, "Terbium", 6)
Dy = Elm(66, 162.5, "Dysprosium", 6)
Ho = Elm(67, 164.93, "Holmium", 6)
Er = Elm(68, 167.259, "Erbium", 6)
Tm = Elm(69, 168.93421, "Thulium", 6)
Yb = Elm(70, 173.04, "Ytterbium", 6)
Lu = Elm(71, 174.967, "Lutetium", 6, 3.0, "III B")
Hf = Elm(72, 178.49, "Hafnium", 6, 4.0, "IV B")
Ta = Elm(73, 180.94788, "Tantalum", 6, 5.0, "V B")
W = Elm(74, 183.84, "Tungsten  (Wolfram)", 6, 6.0, "VI B")
Re = Elm(75, 186.207, "Rhenium", 6, 7.0, "VII B")
Os = Elm(76, 190.23, "Osmium", 6, 8.0, "VIII B")
Ir = Elm(77, 192.217, "Iridium", 6, 9.0, "VIII B")
Pt = Elm(78, 195.084, "Platinum", 6, 10.0, "VIII B")
Au = Elm(79, 196.966569, "Gold  (Aurum)", 6, 11.0, "I B")
Hg = Elm(80, 200.59, "Mercury  (Hydrargyrum)", 6, 12.0, "II B")
Tl = Elm(81, 204.3833, "Thallium", 6, 13.0, "III A")
Pb = Elm(82, 207.2, "Lead  (Plumbum)", 6, 14.0, "IV A")
Bi = Elm(83, 208.9804, "Bismuth", 6, 15.0, "V A")
Po = Elm(84, 210.0, "Polonium", 6, 16.0, "VI A")
At = Elm(85, 210.0, "Astatine", 6, 17.0, "VII A")
Rn = Elm(86, 220.0, "Radon", 6, 18.0, "VIII A")

Fr = Elm(87, 223.0, "Francium", 7, 1.0, "I A")
Ra = Elm(88, 226.0, "Radium", 7, 2.0, "II A")
Ac = Elm(89, 227.0, "Actinium", 7)
Th = Elm(90, 232.03806, "Thorium", 7)
Pa = Elm(91, 231.03588, "Protactinium", 7)
U = Elm(92, 238.02891, "Uranium", 7)
Np = Elm(93, 237.0, "Neptunium", 7)
Pu = Elm(94, 244.0, "Plutonium", 7)
Am = Elm(95, 243.0, "Americium", 7)
Cm = Elm(96, 247.0, "Curium", 7)
Bk = Elm(97, 247.0, "Berkelium", 7)
Cf = Elm(98, 251.0, "Californium", 7)
Es = Elm(99, 252.0, "Einsteinium", 7)
Fm = Elm(100, 257.0, "Fermium", 7)
Md = Elm(101, 258.0, "Mendelevium", 7)
No = Elm(102, 259.0, "Nobelium", 7)
Lr = Elm(103, 262.0, "Lawrencium", 7, 3.0, "III B")
Rf = Elm(104, 261.0, "Rutherfordium", 7, 4.0, "IV B")
Db = Elm(105, 262.0, "Dubnium", 7, 5.0, "V B")
Sg = Elm(106, 266.0, "Seaborgium", 7, 6.0, "VI B")
Bh = Elm(107, 264.0, "Bohrium", 7, 7.0, "VII B")
Hs = Elm(108, 277.0, "Hassium", 7, 8.0, "VIII B")
Mt = Elm(109, 268.0, "Meitnerium", 7, 9.0, "VIII B")
Ds = Elm(110, 271.0, "Darmstadtium", 7, 10.0, "VIII B")
Rg = Elm(111, 272.0, "Roentgenium", 7, 11.0, "I B")
Cn = Elm(112, 285.0, "Copernicium", 7, 12.0, "II B")
Nh = Elm(113, 284.0, "Nihonium", 7, 13.0, "III A")
Fl = Elm(114, 289.0, "Flerovium", 7, 14.0, "IV A")
Mc = Elm(115, 288.0, "Moscovium", 7, 15.0, "V A")
Lv = Elm(116, 292.0, "Livermorium", 7, 16.0, "VI A")
Ts = Elm(117, 292.0, "Tennessine", 7, 16.0, "VI A")
Og = Elm(118, 294.0, "Oganesson", 7, 18.0, "VIII A")

if __name__ == '__main__':
    main()