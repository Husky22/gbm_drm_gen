__author__ = "grburgess"
import numpy as np
import astropy.io.fits as fits

import gbmgeometry

import astropy.units as u

from gbm_drm_gen.drmgen import DRMGen

det_name_lookup = {
    "NAI_00": 0,
    "NAI_01": 1,
    "NAI_02": 2,
    "NAI_03": 3,
    "NAI_04": 4,
    "NAI_05": 5,
    "NAI_06": 6,
    "NAI_07": 7,
    "NAI_08": 8,
    "NAI_09": 9,
    "NAI_10": 10,
    "NAI_11": 11,
    "BGO_00": 12,
    "BGO_01": 13,
}


class DRMGenTTE(DRMGen):
    """
    A TTE/CSPEC specific drmgen already incorporating the standard input edges. Output edges are obtained
    from the input cspec file. Spacecraft position is read from the TTE file. For further details see the 
    generic reader (DRMGen).

    :param trigdat: the path to a trigdat file
    :param det: the number (0-13) of the detector to be used
    :param mat_type: 0=direct 1=scattered 2=direct+scattered
    :param time: time relative to trigger to pull spacecraft position or MET if using a poshist file
    :param cspecfile: the cspecfile to pull energy output edges from
    :param poshist: read a poshist file
    """

    def __init__(
        self,
        tte_file,
        time=0.0,
        cspecfile=None,
        trigdat=None,
        poshist=None,
        T0=None,
        mat_type=0,
        occult=False,
    ):

        self._occult = occult

        self._time = time

        self._matrix_type = mat_type

        with fits.open(tte_file) as f:

            det_name = f["PRIMARY"].header["DETNAM"]

        self._det_number = det_name_lookup[det_name]

        if self._det_number > 11:
            # BGO
            self._in_edge = np.array(
                [
                    100.000,
                    105.579,
                    111.470,
                    117.689,
                    124.255,
                    131.188,
                    138.507,
                    146.235,
                    154.394,
                    163.008,
                    172.103,
                    181.705,
                    191.843,
                    202.546,
                    213.847,
                    225.778,
                    238.375,
                    251.675,
                    265.716,
                    280.541,
                    296.194,
                    312.719,
                    330.167,
                    348.588,
                    368.036,
                    388.570,
                    410.250,
                    433.139,
                    457.305,
                    482.820,
                    509.757,
                    538.198,
                    568.226,
                    599.929,
                    633.401,
                    668.740,
                    706.052,
                    745.444,
                    787.035,
                    830.946,
                    877.307,
                    926.255,
                    977.933,
                    1032.49,
                    1090.10,
                    1150.92,
                    1215.13,
                    1282.93,
                    1354.51,
                    1430.08,
                    1509.87,
                    1594.11,
                    1683.05,
                    1776.95,
                    1876.09,
                    1980.77,
                    2091.28,
                    2207.96,
                    2331.15,
                    2461.21,
                    2598.53,
                    2743.51,
                    2896.58,
                    3058.18,
                    3228.81,
                    3408.95,
                    3599.15,
                    3799.96,
                    4011.97,
                    4235.81,
                    4472.14,
                    4721.65,
                    4985.09,
                    5263.22,
                    5556.87,
                    5866.90,
                    6194.24,
                    6539.83,
                    6904.71,
                    7289.95,
                    7696.67,
                    8126.09,
                    8579.47,
                    9058.15,
                    9563.53,
                    10097.1,
                    10660.5,
                    11255.2,
                    11883.2,
                    12546.2,
                    13246.2,
                    13985.2,
                    14765.5,
                    15589.3,
                    16459.1,
                    17377.4,
                    18346.9,
                    19370.6,
                    20451.3,
                    21592.4,
                    22797.1,
                    24069.0,
                    25411.8,
                    26829.7,
                    28326.6,
                    29907.0,
                    31575.6,
                    33337.3,
                    35197.3,
                    37161.0,
                    39234.4,
                    41423.4,
                    43734.5,
                    46174.6,
                    48750.8,
                    51470.7,
                    54342.5,
                    57374.4,
                    60575.5,
                    63955.2,
                    67523.4,
                    71290.7,
                    75268.2,
                    79467.7,
                    83901.5,
                    88582.6,
                    93524.9,
                    98742.9,
                    104252.0,
                    110069.0,
                    116210.0,
                    122693.0,
                    129539.0,
                    136766.0,
                    144397.0,
                    152453.0,
                    160959.0,
                    169939.0,
                    179421.0,
                    189431.0,
                    200000.0,
                ],
                dtype=np.float32,
            )

        else:
            self._in_edge = np.array(
                [
                    5.00000,
                    5.34000,
                    5.70312,
                    6.09094,
                    6.50513,
                    6.94748,
                    7.41991,
                    7.92447,
                    8.46333,
                    9.03884,
                    9.65349,
                    10.3099,
                    11.0110,
                    11.7598,
                    12.5594,
                    13.4135,
                    14.3256,
                    15.2997,
                    16.3401,
                    17.4513,
                    18.6380,
                    19.9054,
                    21.2589,
                    22.7045,
                    24.2485,
                    25.8974,
                    27.6584,
                    29.5392,
                    31.5479,
                    33.6931,
                    35.9843,
                    38.4312,
                    41.0446,
                    43.8356,
                    46.8164,
                    50.0000,
                    53.4000,
                    57.0312,
                    60.9094,
                    65.0513,
                    69.4748,
                    74.1991,
                    79.2446,
                    84.6333,
                    90.3884,
                    96.5349,
                    103.099,
                    110.110,
                    117.598,
                    125.594,
                    134.135,
                    143.256,
                    152.997,
                    163.401,
                    174.513,
                    186.380,
                    199.054,
                    212.589,
                    227.045,
                    242.485,
                    258.974,
                    276.584,
                    295.392,
                    315.479,
                    336.931,
                    359.843,
                    384.312,
                    410.446,
                    438.356,
                    468.164,
                    500.000,
                    534.000,
                    570.312,
                    609.094,
                    650.512,
                    694.748,
                    741.991,
                    792.446,
                    846.333,
                    903.884,
                    965.349,
                    1030.99,
                    1101.10,
                    1175.98,
                    1255.94,
                    1341.35,
                    1432.56,
                    1529.97,
                    1634.01,
                    1745.13,
                    1863.80,
                    1990.54,
                    2125.89,
                    2270.45,
                    2424.85,
                    2589.74,
                    2765.84,
                    2953.92,
                    3154.79,
                    3369.31,
                    3598.43,
                    3843.12,
                    4104.46,
                    4383.56,
                    4681.65,
                    5000.00,
                    5340.00,
                    5703.12,
                    6090.94,
                    6505.12,
                    6947.48,
                    7419.91,
                    7924.46,
                    8463.33,
                    9038.84,
                    9653.49,
                    10309.9,
                    11011.0,
                    11759.8,
                    12559.4,
                    13413.5,
                    14325.6,
                    15299.7,
                    16340.1,
                    17451.3,
                    18637.9,
                    19905.3,
                    21258.9,
                    22704.5,
                    24248.5,
                    25897.3,
                    27658.4,
                    29539.2,
                    31547.8,
                    33693.1,
                    35984.3,
                    38431.2,
                    41044.6,
                    43835.6,
                    46816.4,
                    50000.0,
                ],
                dtype=np.float32,
            )

        # Create the out edge energies
        with fits.open(cspecfile) as f:
            out_edge = np.zeros(129, dtype=np.float32)
            out_edge[:-1] = f["EBOUNDS"].data["E_MIN"]
            out_edge[-1] = f["EBOUNDS"].data["E_MAX"][-1]

        self._out_edge = out_edge

        # if poshist is None:
        #
        #     self._use_poshist = False
        #
        #     # Space craft stuff from TRIGDAT
        #     with fits.open(trigdat) as f:
        #         self._trigtime = f['EVNTRATE'].header['TRIGTIME']
        #
        #         self._tstart = f['EVNTRATE'].data['TIME'] - self._trigtime
        #         self._tstop = f['EVNTRATE'].data['ENDTIME'] - self._trigtime
        #
        #         self._all_quats = f['EVNTRATE'].data['SCATTITD']
        #         self._all_sc_pos = f['EVNTRATE'].data['EIC']
        #

        # this uses the trigger time!

        #
        # elif trigdat is None:
        #
        #     self._use_poshist = True
        #
        #     with fits.open(poshist) as f:
        #
        #         self._poshist_time = f['GLAST POS HIST'].data['SCLK_UTC']
        #
        #         self._q1 = f['GLAST POS HIST'].data['QSJ_1']
        #         self._q2 = f['GLAST POS HIST'].data['QSJ_2']
        #         self._q3 = f['GLAST POS HIST'].data['QSJ_3']
        #         self._q4 = f['GLAST POS HIST'].data['QSJ_4']
        #
        #         self._pos_X = f['GLAST POS HIST'].data['POS_X']
        #         self._pos_Y = f['GLAST POS HIST'].data['POS_Y']
        #         self._pos_Z = f['GLAST POS HIST'].data['POS_Z']

        if trigdat is not None:

            self._position_interpolator = gbmgeometry.PositionInterpolator(
                trigdat=trigdat
            )

            self._gbm = gbmgeometry.GBM(
                self._position_interpolator.quaternion(time),
                self._position_interpolator.sc_pos(time) * u.km,
            )

        elif poshist is not None:

            self._position_interpolator = gbmgeometry.PositionInterpolator(
                poshist=poshist, T0=T0
            )

            self._gbm = gbmgeometry.GBM(
                self._position_interpolator.quaternion(time),
                self._position_interpolator.sc_pos(time) * u.m,
            )

        else:

            raise RuntimeError("No trigdat or posthist file used!")

        self._sc_quaternions_updater()

    def _sc_quaternions_updater(self):
        #
        # if self._use_poshist:
        #
        #     condition = np.argmin(self._poshist_time - self._time)
        #
        #     quaternions = np.array([self._q1[condition],
        #                             self._q2[condition],
        #                             self._q3[condition],
        #                             self._q4[condition]])
        #
        #     sc_pos = np.array([self._pos_X[condition],
        #                        self._pos_Y[condition],
        #                        self._pos_Z[condition]])
        #
        # else:
        #
        #     condition = np.logical_and(self._tstart <= self._time, self._time <= self._tstop)
        #
        #     quaternions = self._all_quats[condition][0]
        #     sc_pos = self._all_sc_pos[condition][0]

        quaternions = self._position_interpolator.quaternion(self._time)

        sc_pos = self._position_interpolator.sc_pos(self._time)


        super(DRMGenTTE, self).__init__(quaternions=quaternions,
                                        sc_pos=sc_pos,
                                        det_number=self._det_number,
                                        ebin_edge_in=self._in_edge,
                                        mat_type=self._matrix_type,
                                        ebin_edge_out=self._out_edge,
                                        occult=self._occult)

