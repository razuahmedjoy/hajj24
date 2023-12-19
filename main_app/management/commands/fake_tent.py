import random
import string
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from main_app.models import Tent, Camera
from main_app.api.serializers import TentSerializer, CameraSerializer

User = get_user_model()

tent_data = [
  {
    "name": "Hajj demo event 1",
    "lat": -32.3936,
    "long": 47.277462,
    "location": "Highland"
  },
  {
    "name": "Hajj demo event 2",
    "lat": 73.220232,
    "long": -16.303487,
    "location": "Bakersville"
  },
  {
    "name": "Hajj demo event 3",
    "lat": 81.174491,
    "long": 31.923011,
    "location": "Hayes"
  },
  {
    "name": "Hajj demo event 4",
    "lat": -49.756279,
    "long": -138.77738,
    "location": "Esmont"
  },
  {
    "name": "Hajj demo event 5",
    "lat": 43.026486,
    "long": 41.379157,
    "location": "Wauhillau"
  },
  {
    "name": "Hajj demo event 6",
    "lat": -29.938722,
    "long": 130.923733,
    "location": "Grimsley"
  },
  {
    "name": "Hajj demo event 7",
    "lat": 32.198678,
    "long": 170.095076,
    "location": "Cloverdale"
  },
  {
    "name": "Hajj demo event 8",
    "lat": 89.657293,
    "long": 33.981641,
    "location": "Emison"
  },
  {
    "name": "Hajj demo event 9",
    "lat": -70.375855,
    "long": 5.165333,
    "location": "Clarksburg"
  },
  {
    "name": "Hajj demo event 10",
    "lat": -47.263557,
    "long": 83.665953,
    "location": "Crucible"
  },
  {
    "name": "Hajj demo event 11",
    "lat": 58.8622,
    "long": -70.792975,
    "location": "Rosewood"
  },
  {
    "name": "Hajj demo event 12",
    "lat": -0.980941,
    "long": -87.064615,
    "location": "Dotsero"
  },
  {
    "name": "Hajj demo event 13",
    "lat": 34.557035,
    "long": -65.552647,
    "location": "Skyland"
  },
  {
    "name": "Hajj demo event 14",
    "lat": -8.333633,
    "long": -130.489898,
    "location": "Advance"
  },
  {
    "name": "Hajj demo event 15",
    "lat": 84.692288,
    "long": -99.505927,
    "location": "Waterford"
  },
  {
    "name": "Hajj demo event 16",
    "lat": -62.648069,
    "long": 174.769602,
    "location": "Tuttle"
  },
  {
    "name": "Hajj demo event 17",
    "lat": 77.272194,
    "long": -1.497255,
    "location": "Bowden"
  },
  {
    "name": "Hajj demo event 18",
    "lat": -10.900651,
    "long": -174.036998,
    "location": "Dowling"
  },
  {
    "name": "Hajj demo event 19",
    "lat": -60.692654,
    "long": 38.341457,
    "location": "Navarre"
  },
  {
    "name": "Hajj demo event 20",
    "lat": 6.910791,
    "long": 133.672363,
    "location": "Moraida"
  },
  {
    "name": "Hajj demo event 21",
    "lat": 8.779467,
    "long": -37.010871,
    "location": "Vienna"
  },
  {
    "name": "Hajj demo event 22",
    "lat": -81.251904,
    "long": -82.905787,
    "location": "Brule"
  },
  {
    "name": "Hajj demo event 23",
    "lat": 18.540304,
    "long": -85.496996,
    "location": "Nipinnawasee"
  },
  {
    "name": "Hajj demo event 24",
    "lat": 55.061698,
    "long": -127.109043,
    "location": "Goochland"
  },
  {
    "name": "Hajj demo event 25",
    "lat": -49.378357,
    "long": -67.157824,
    "location": "Basye"
  },
  {
    "name": "Hajj demo event 26",
    "lat": -52.786446,
    "long": 67.615092,
    "location": "Austinburg"
  },
  {
    "name": "Hajj demo event 27",
    "lat": -55.562289,
    "long": -63.946361,
    "location": "Mansfield"
  },
  {
    "name": "Hajj demo event 28",
    "lat": -7.875157,
    "long": 94.129524,
    "location": "Terlingua"
  },
  {
    "name": "Hajj demo event 29",
    "lat": -55.051321,
    "long": -104.781772,
    "location": "Lorraine"
  },
  {
    "name": "Hajj demo event 30",
    "lat": -39.351906,
    "long": 104.244664,
    "location": "Norris"
  },
  {
    "name": "Hajj demo event 31",
    "lat": -84.07999,
    "long": 115.918167,
    "location": "Bellfountain"
  },
  {
    "name": "Hajj demo event 32",
    "lat": 86.877869,
    "long": -174.699434,
    "location": "Elliott"
  },
  {
    "name": "Hajj demo event 33",
    "lat": 79.607557,
    "long": -120.833696,
    "location": "Hailesboro"
  },
  {
    "name": "Hajj demo event 34",
    "lat": -39.03231,
    "long": -19.221866,
    "location": "Idledale"
  },
  {
    "name": "Hajj demo event 35",
    "lat": 81.156409,
    "long": -145.480675,
    "location": "Chemung"
  },
  {
    "name": "Hajj demo event 36",
    "lat": 33.998187,
    "long": -174.706923,
    "location": "Bethany"
  },
  {
    "name": "Hajj demo event 37",
    "lat": 4.261927,
    "long": 92.282936,
    "location": "Rosburg"
  },
  {
    "name": "Hajj demo event 38",
    "lat": 26.349783,
    "long": -89.555564,
    "location": "Blackgum"
  },
  {
    "name": "Hajj demo event 39",
    "lat": -64.693192,
    "long": -157.616842,
    "location": "Dahlen"
  },
  {
    "name": "Hajj demo event 40",
    "lat": 24.915802,
    "long": 57.348505,
    "location": "Summerset"
  },
  {
    "name": "Hajj demo event 41",
    "lat": -65.510142,
    "long": -167.94905,
    "location": "Axis"
  },
  {
    "name": "Hajj demo event 42",
    "lat": -9.368284,
    "long": -34.537793,
    "location": "Riceville"
  },
  {
    "name": "Hajj demo event 43",
    "lat": 72.973422,
    "long": -88.969486,
    "location": "Tilden"
  },
  {
    "name": "Hajj demo event 44",
    "lat": 39.446521,
    "long": -50.815518,
    "location": "Vivian"
  },
  {
    "name": "Hajj demo event 45",
    "lat": 24.536102,
    "long": -120.202455,
    "location": "Veyo"
  },
  {
    "name": "Hajj demo event 46",
    "lat": -11.587317,
    "long": 53.168973,
    "location": "Thermal"
  },
  {
    "name": "Hajj demo event 47",
    "lat": -62.148652,
    "long": -76.020076,
    "location": "Jennings"
  },
  {
    "name": "Hajj demo event 48",
    "lat": 79.273644,
    "long": -165.176754,
    "location": "Alafaya"
  },
  {
    "name": "Hajj demo event 49",
    "lat": -30.396753,
    "long": -3.127794,
    "location": "Cavalero"
  },
  {
    "name": "Hajj demo event 50",
    "lat": -22.131416,
    "long": 49.70248,
    "location": "Welch"
  },
  {
    "name": "Hajj demo event 51",
    "lat": -48.029782,
    "long": -18.438668,
    "location": "Eastmont"
  },
  {
    "name": "Hajj demo event 52",
    "lat": -51.581252,
    "long": 111.740079,
    "location": "Abiquiu"
  },
  {
    "name": "Hajj demo event 53",
    "lat": 71.569643,
    "long": 97.638628,
    "location": "Frierson"
  },
  {
    "name": "Hajj demo event 54",
    "lat": -70.839389,
    "long": -115.881174,
    "location": "Robinette"
  },
  {
    "name": "Hajj demo event 55",
    "lat": -4.629251,
    "long": -159.818788,
    "location": "Seymour"
  },
  {
    "name": "Hajj demo event 56",
    "lat": -41.66983,
    "long": -92.935777,
    "location": "Clinton"
  },
  {
    "name": "Hajj demo event 57",
    "lat": -29.065272,
    "long": -18.855496,
    "location": "Coultervillle"
  },
  {
    "name": "Hajj demo event 58",
    "lat": -67.355848,
    "long": 112.367504,
    "location": "Coleville"
  },
  {
    "name": "Hajj demo event 59",
    "lat": 3.980814,
    "long": 149.327487,
    "location": "Osage"
  },
  {
    "name": "Hajj demo event 60",
    "lat": -86.387293,
    "long": -75.8519,
    "location": "Caroleen"
  },
  {
    "name": "Hajj demo event 61",
    "lat": 12.10854,
    "long": -43.076933,
    "location": "Frizzleburg"
  },
  {
    "name": "Hajj demo event 62",
    "lat": -21.335395,
    "long": -107.223293,
    "location": "Nescatunga"
  },
  {
    "name": "Hajj demo event 63",
    "lat": 6.315225,
    "long": -161.457581,
    "location": "Enlow"
  },
  {
    "name": "Hajj demo event 64",
    "lat": -33.996468,
    "long": -174.310145,
    "location": "Detroit"
  },
  {
    "name": "Hajj demo event 65",
    "lat": -43.881433,
    "long": -62.773945,
    "location": "Osmond"
  },
  {
    "name": "Hajj demo event 66",
    "lat": -27.09479,
    "long": -82.551472,
    "location": "Glidden"
  },
  {
    "name": "Hajj demo event 67",
    "lat": 62.595737,
    "long": -66.285205,
    "location": "Byrnedale"
  },
  {
    "name": "Hajj demo event 68",
    "lat": -10.428365,
    "long": -165.478514,
    "location": "Omar"
  },
  {
    "name": "Hajj demo event 69",
    "lat": -1.932027,
    "long": -33.305822,
    "location": "Jeff"
  },
  {
    "name": "Hajj demo event 70",
    "lat": -13.298855,
    "long": 73.780004,
    "location": "Nicut"
  },
  {
    "name": "Hajj demo event 71",
    "lat": 57.252782,
    "long": -88.149228,
    "location": "Castleton"
  },
  {
    "name": "Hajj demo event 72",
    "lat": 79.649643,
    "long": -139.495183,
    "location": "Delwood"
  },
  {
    "name": "Hajj demo event 73",
    "lat": -84.393328,
    "long": 94.724415,
    "location": "Turpin"
  },
  {
    "name": "Hajj demo event 74",
    "lat": 49.626682,
    "long": 63.678245,
    "location": "Boomer"
  },
  {
    "name": "Hajj demo event 75",
    "lat": -17.775406,
    "long": -70.253684,
    "location": "Catharine"
  },
  {
    "name": "Hajj demo event 76",
    "lat": -45.431406,
    "long": 91.683727,
    "location": "Summertown"
  },
  {
    "name": "Hajj demo event 77",
    "lat": 53.640966,
    "long": 27.51713,
    "location": "Longbranch"
  },
  {
    "name": "Hajj demo event 78",
    "lat": -56.004495,
    "long": 58.911482,
    "location": "Cutter"
  },
  {
    "name": "Hajj demo event 79",
    "lat": -9.971855,
    "long": -56.52193,
    "location": "Beechmont"
  },
  {
    "name": "Hajj demo event 80",
    "lat": -19.710393,
    "long": -97.661246,
    "location": "Matthews"
  },
  {
    "name": "Hajj demo event 81",
    "lat": -49.695146,
    "long": -41.876992,
    "location": "Iola"
  },
  {
    "name": "Hajj demo event 82",
    "lat": 46.852883,
    "long": 87.811537,
    "location": "Cressey"
  },
  {
    "name": "Hajj demo event 83",
    "lat": 71.115052,
    "long": -15.148809,
    "location": "Calpine"
  },
  {
    "name": "Hajj demo event 84",
    "lat": -46.609698,
    "long": 60.254769,
    "location": "Grahamtown"
  },
  {
    "name": "Hajj demo event 85",
    "lat": 21.957808,
    "long": 79.588117,
    "location": "Verdi"
  },
  {
    "name": "Hajj demo event 86",
    "lat": -40.032542,
    "long": 66.788606,
    "location": "Condon"
  },
  {
    "name": "Hajj demo event 87",
    "lat": 80.340359,
    "long": -79.975573,
    "location": "Cleary"
  },
  {
    "name": "Hajj demo event 88",
    "lat": 9.511804,
    "long": 121.284304,
    "location": "Datil"
  },
  {
    "name": "Hajj demo event 89",
    "lat": -15.310968,
    "long": 61.496963,
    "location": "Bridgetown"
  },
  {
    "name": "Hajj demo event 90",
    "lat": -28.880899,
    "long": 79.542272,
    "location": "Shrewsbury"
  },
  {
    "name": "Hajj demo event 91",
    "lat": 70.500556,
    "long": 149.470699,
    "location": "Konterra"
  },
  {
    "name": "Hajj demo event 92",
    "lat": 46.450105,
    "long": 159.833559,
    "location": "Carrizo"
  },
  {
    "name": "Hajj demo event 93",
    "lat": 75.065264,
    "long": -77.425147,
    "location": "Whitehaven"
  },
  {
    "name": "Hajj demo event 94",
    "lat": -66.150088,
    "long": 14.459033,
    "location": "Topanga"
  },
  {
    "name": "Hajj demo event 95",
    "lat": -8.983623,
    "long": -79.080675,
    "location": "Gibbsville"
  },
  {
    "name": "Hajj demo event 96",
    "lat": -46.201737,
    "long": -114.873763,
    "location": "Fairforest"
  },
  {
    "name": "Hajj demo event 97",
    "lat": -82.724582,
    "long": 18.332347,
    "location": "Avalon"
  },
  {
    "name": "Hajj demo event 98",
    "lat": -66.510252,
    "long": 154.579493,
    "location": "Haena"
  },
  {
    "name": "Hajj demo event 99",
    "lat": -49.831476,
    "long": 78.850869,
    "location": "Guilford"
  },
  {
    "name": "Hajj demo event 100",
    "lat": 88.212887,
    "long": 69.237297,
    "location": "Diaperville"
  },
  {
    "name": "Hajj demo event 101",
    "lat": 89.517196,
    "long": 13.148479,
    "location": "Cochranville"
  },
  {
    "name": "Hajj demo event 102",
    "lat": 52.673537,
    "long": 47.337894,
    "location": "Winesburg"
  },
  {
    "name": "Hajj demo event 103",
    "lat": 77.816152,
    "long": 128.578903,
    "location": "Veguita"
  },
  {
    "name": "Hajj demo event 104",
    "lat": 39.985955,
    "long": 98.473062,
    "location": "Holcombe"
  },
  {
    "name": "Hajj demo event 105",
    "lat": -41.20467,
    "long": 100.451958,
    "location": "Virgie"
  },
  {
    "name": "Hajj demo event 106",
    "lat": -46.962461,
    "long": 13.843608,
    "location": "Chapin"
  },
  {
    "name": "Hajj demo event 107",
    "lat": 55.299629,
    "long": -8.186135,
    "location": "Hinsdale"
  },
  {
    "name": "Hajj demo event 108",
    "lat": -85.311142,
    "long": 149.536654,
    "location": "Saddlebrooke"
  },
  {
    "name": "Hajj demo event 109",
    "lat": 27.315537,
    "long": 48.082391,
    "location": "Dale"
  },
  {
    "name": "Hajj demo event 110",
    "lat": -14.173535,
    "long": 48.271025,
    "location": "Canterwood"
  },
  {
    "name": "Hajj demo event 111",
    "lat": -51.3616,
    "long": 178.313509,
    "location": "Efland"
  },
  {
    "name": "Hajj demo event 112",
    "lat": 86.870832,
    "long": 28.311706,
    "location": "Shindler"
  },
  {
    "name": "Hajj demo event 113",
    "lat": 68.880406,
    "long": -143.493101,
    "location": "Needmore"
  },
  {
    "name": "Hajj demo event 114",
    "lat": 41.45243,
    "long": -12.593129,
    "location": "Hamilton"
  },
  {
    "name": "Hajj demo event 115",
    "lat": 9.353125,
    "long": 64.651594,
    "location": "Drummond"
  },
  {
    "name": "Hajj demo event 116",
    "lat": -12.142097,
    "long": -102.047799,
    "location": "Bison"
  },
  {
    "name": "Hajj demo event 117",
    "lat": 12.515633,
    "long": -24.499822,
    "location": "Sunnyside"
  },
  {
    "name": "Hajj demo event 118",
    "lat": 85.743958,
    "long": 81.013792,
    "location": "Kieler"
  },
  {
    "name": "Hajj demo event 119",
    "lat": -17.429421,
    "long": 141.64249,
    "location": "Chical"
  },
  {
    "name": "Hajj demo event 120",
    "lat": 57.919414,
    "long": 134.873954,
    "location": "Homeworth"
  },
  {
    "name": "Hajj demo event 121",
    "lat": -60.605584,
    "long": 178.398487,
    "location": "Rockbridge"
  },
  {
    "name": "Hajj demo event 122",
    "lat": -51.070315,
    "long": -69.855516,
    "location": "Cobbtown"
  },
  {
    "name": "Hajj demo event 123",
    "lat": -65.62425,
    "long": -30.988183,
    "location": "Drytown"
  },
  {
    "name": "Hajj demo event 124",
    "lat": -68.752178,
    "long": -30.184675,
    "location": "Gerton"
  },
  {
    "name": "Hajj demo event 125",
    "lat": 87.788584,
    "long": 114.239028,
    "location": "Bayview"
  },
  {
    "name": "Hajj demo event 126",
    "lat": -24.793022,
    "long": -161.224173,
    "location": "Connerton"
  },
  {
    "name": "Hajj demo event 127",
    "lat": -54.676824,
    "long": -39.087066,
    "location": "Babb"
  },
  {
    "name": "Hajj demo event 128",
    "lat": -35.619241,
    "long": -76.870507,
    "location": "Sutton"
  },
  {
    "name": "Hajj demo event 129",
    "lat": -43.168969,
    "long": -27.044804,
    "location": "Weedville"
  },
  {
    "name": "Hajj demo event 130",
    "lat": 36.599914,
    "long": -164.571685,
    "location": "Jacksonburg"
  },
  {
    "name": "Hajj demo event 131",
    "lat": -42.315239,
    "long": 86.128905,
    "location": "Richford"
  },
  {
    "name": "Hajj demo event 132",
    "lat": -75.385805,
    "long": 30.318456,
    "location": "Waumandee"
  },
  {
    "name": "Hajj demo event 133",
    "lat": 27.503331,
    "long": -25.473632,
    "location": "Ferney"
  },
  {
    "name": "Hajj demo event 134",
    "lat": -45.024786,
    "long": -167.320519,
    "location": "Bradenville"
  },
  {
    "name": "Hajj demo event 135",
    "lat": -67.488241,
    "long": 60.678756,
    "location": "Williams"
  },
  {
    "name": "Hajj demo event 136",
    "lat": 35.56438,
    "long": 178.392903,
    "location": "Independence"
  },
  {
    "name": "Hajj demo event 137",
    "lat": 6.172895,
    "long": -101.864194,
    "location": "Westboro"
  },
  {
    "name": "Hajj demo event 138",
    "lat": 11.045512,
    "long": 176.431558,
    "location": "Retsof"
  },
  {
    "name": "Hajj demo event 139",
    "lat": -10.942598,
    "long": -58.835656,
    "location": "Waterloo"
  },
  {
    "name": "Hajj demo event 140",
    "lat": -12.61569,
    "long": 156.134685,
    "location": "Newkirk"
  },
  {
    "name": "Hajj demo event 141",
    "lat": -81.04021,
    "long": 35.083701,
    "location": "Nadine"
  },
  {
    "name": "Hajj demo event 142",
    "lat": 87.65224,
    "long": 114.909341,
    "location": "Catherine"
  },
  {
    "name": "Hajj demo event 143",
    "lat": -68.607899,
    "long": 78.680432,
    "location": "Thornport"
  },
  {
    "name": "Hajj demo event 144",
    "lat": 80.816801,
    "long": -142.30894,
    "location": "Savage"
  },
  {
    "name": "Hajj demo event 145",
    "lat": -67.748096,
    "long": -1.908897,
    "location": "Riviera"
  },
  {
    "name": "Hajj demo event 146",
    "lat": -2.389567,
    "long": 127.684215,
    "location": "Hollymead"
  },
  {
    "name": "Hajj demo event 147",
    "lat": 70.250257,
    "long": 71.437506,
    "location": "Wawona"
  },
  {
    "name": "Hajj demo event 148",
    "lat": -86.926269,
    "long": -90.292189,
    "location": "Fontanelle"
  },
  {
    "name": "Hajj demo event 149",
    "lat": -15.54185,
    "long": 95.389763,
    "location": "Riner"
  },
  {
    "name": "Hajj demo event 150",
    "lat": -9.722025,
    "long": 65.268751,
    "location": "Cliffside"
  },
  {
    "name": "Hajj demo event 151",
    "lat": -3.152269,
    "long": 175.291293,
    "location": "Farmers"
  },
  {
    "name": "Hajj demo event 152",
    "lat": 57.443826,
    "long": -65.591706,
    "location": "Hessville"
  },
  {
    "name": "Hajj demo event 153",
    "lat": -64.906978,
    "long": 155.81753,
    "location": "Bainbridge"
  },
  {
    "name": "Hajj demo event 154",
    "lat": 80.63871,
    "long": 101.786392,
    "location": "Dixonville"
  },
  {
    "name": "Hajj demo event 155",
    "lat": -41.990788,
    "long": -42.21424,
    "location": "Groton"
  },
  {
    "name": "Hajj demo event 156",
    "lat": 23.831781,
    "long": -116.976547,
    "location": "Marne"
  },
  {
    "name": "Hajj demo event 157",
    "lat": -37.81087,
    "long": -152.317053,
    "location": "Coaldale"
  },
  {
    "name": "Hajj demo event 158",
    "lat": 7.514258,
    "long": 164.499769,
    "location": "Ola"
  },
  {
    "name": "Hajj demo event 159",
    "lat": 61.685972,
    "long": -65.214782,
    "location": "Foxworth"
  },
  {
    "name": "Hajj demo event 160",
    "lat": 72.484883,
    "long": 173.806471,
    "location": "Weogufka"
  },
  {
    "name": "Hajj demo event 161",
    "lat": 78.246903,
    "long": -15.766481,
    "location": "Toftrees"
  },
  {
    "name": "Hajj demo event 162",
    "lat": -4.062391,
    "long": -134.438146,
    "location": "Collins"
  },
  {
    "name": "Hajj demo event 163",
    "lat": -64.986203,
    "long": 144.27177,
    "location": "Hollins"
  },
  {
    "name": "Hajj demo event 164",
    "lat": 46.358936,
    "long": -152.781794,
    "location": "Elwood"
  },
  {
    "name": "Hajj demo event 165",
    "lat": 34.753734,
    "long": 51.947823,
    "location": "Nelson"
  },
  {
    "name": "Hajj demo event 166",
    "lat": 11.008549,
    "long": 13.813189,
    "location": "Ypsilanti"
  },
  {
    "name": "Hajj demo event 167",
    "lat": 62.987213,
    "long": -49.348739,
    "location": "Durham"
  },
  {
    "name": "Hajj demo event 168",
    "lat": 6.783436,
    "long": 14.00385,
    "location": "Hachita"
  },
  {
    "name": "Hajj demo event 169",
    "lat": 37.638811,
    "long": -166.809661,
    "location": "Alfarata"
  },
  {
    "name": "Hajj demo event 170",
    "lat": 3.695895,
    "long": 138.459682,
    "location": "Tioga"
  },
  {
    "name": "Hajj demo event 171",
    "lat": 42.865044,
    "long": -101.979802,
    "location": "Dodge"
  },
  {
    "name": "Hajj demo event 172",
    "lat": -34.599773,
    "long": 68.192602,
    "location": "Riverton"
  },
  {
    "name": "Hajj demo event 173",
    "lat": -13.510661,
    "long": 117.877725,
    "location": "Reinerton"
  },
  {
    "name": "Hajj demo event 174",
    "lat": -77.231127,
    "long": -112.699303,
    "location": "Conestoga"
  },
  {
    "name": "Hajj demo event 175",
    "lat": -51.414299,
    "long": -7.007623,
    "location": "Finzel"
  },
  {
    "name": "Hajj demo event 176",
    "lat": -49.354086,
    "long": -148.291556,
    "location": "Turah"
  },
  {
    "name": "Hajj demo event 177",
    "lat": -44.871267,
    "long": -79.64062,
    "location": "Baker"
  },
  {
    "name": "Hajj demo event 178",
    "lat": -12.063087,
    "long": 125.571325,
    "location": "Hayden"
  },
  {
    "name": "Hajj demo event 179",
    "lat": -27.282059,
    "long": -53.077533,
    "location": "Tibbie"
  },
  {
    "name": "Hajj demo event 180",
    "lat": -89.710816,
    "long": -48.369283,
    "location": "Gilmore"
  },
  {
    "name": "Hajj demo event 181",
    "lat": -67.083175,
    "long": -65.117505,
    "location": "Waukeenah"
  },
  {
    "name": "Hajj demo event 182",
    "lat": -17.594968,
    "long": -72.672996,
    "location": "Broadlands"
  },
  {
    "name": "Hajj demo event 183",
    "lat": -71.194794,
    "long": -46.708631,
    "location": "Chalfant"
  },
  {
    "name": "Hajj demo event 184",
    "lat": 37.150439,
    "long": -102.123635,
    "location": "Barclay"
  },
  {
    "name": "Hajj demo event 185",
    "lat": 58.834197,
    "long": -30.095478,
    "location": "Alden"
  },
  {
    "name": "Hajj demo event 186",
    "lat": 12.659408,
    "long": 127.39339,
    "location": "Geyserville"
  },
  {
    "name": "Hajj demo event 187",
    "lat": 24.645615,
    "long": -31.894253,
    "location": "Shepardsville"
  },
  {
    "name": "Hajj demo event 188",
    "lat": 50.913048,
    "long": -80.298348,
    "location": "Taft"
  },
  {
    "name": "Hajj demo event 189",
    "lat": 39.662022,
    "long": -124.906319,
    "location": "Moquino"
  },
  {
    "name": "Hajj demo event 190",
    "lat": -60.532894,
    "long": -41.975652,
    "location": "Martinez"
  },
  {
    "name": "Hajj demo event 191",
    "lat": -47.998487,
    "long": -137.126745,
    "location": "Williamson"
  },
  {
    "name": "Hajj demo event 192",
    "lat": -5.478587,
    "long": 166.435343,
    "location": "Waterview"
  },
  {
    "name": "Hajj demo event 193",
    "lat": 75.689802,
    "long": -43.825902,
    "location": "Orovada"
  },
  {
    "name": "Hajj demo event 194",
    "lat": -6.036967,
    "long": 82.576962,
    "location": "Manitou"
  },
  {
    "name": "Hajj demo event 195",
    "lat": -13.029214,
    "long": -130.735033,
    "location": "Lithium"
  },
  {
    "name": "Hajj demo event 196",
    "lat": 9.282648,
    "long": -35.45568,
    "location": "Beyerville"
  },
  {
    "name": "Hajj demo event 197",
    "lat": 60.18884,
    "long": -21.749121,
    "location": "Townsend"
  },
  {
    "name": "Hajj demo event 198",
    "lat": 81.008556,
    "long": 173.285958,
    "location": "Santel"
  },
  {
    "name": "Hajj demo event 199",
    "lat": 27.513879,
    "long": 68.536359,
    "location": "Brooktrails"
  },
  {
    "name": "Hajj demo event 200",
    "lat": -51.575294,
    "long": -121.548114,
    "location": "Makena"
  }
]


class Command(BaseCommand):
    help = 'Create fake data for tents with empty arrays for cameras'

    def generate_random_sn(self):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(16))

    def handle(self, *args, **options):
        users = User.objects.all()

        try:
            with transaction.atomic():
                for tent_info in tent_data:
                    tent_info["created_by"] = random.choice(users).id
                    tent_serializer = TentSerializer(data=tent_info)
                    if tent_serializer.is_valid():
                        tent = tent_serializer.save()

        except Exception as e:
            print(f"Error creating tents with empty arrays for cameras: {e}")
