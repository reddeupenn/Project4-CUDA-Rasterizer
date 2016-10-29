import matplotlib.pyplot as plt
import numpy as np


# bbox backface culling and sorting
p1 = [[0.365696, 49.720222, 0.000000, 0.886528, 0.000000],
[0.589344, 49.664959, 0.000000, 0.887264, 0.000000],
[0.334112, 49.678818, 0.000000, 0.885408, 0.000000],
[0.322304, 49.711166, 0.000000, 0.884512, 0.000000],
[0.326880, 49.688255, 0.000000, 0.887008, 0.000000],
[0.333536, 49.709217, 0.000000, 0.890496, 0.000000],
[0.424448, 49.668385, 0.000000, 0.887168, 0.000000],
[0.287072, 49.726593, 0.000000, 0.883040, 0.000000],
[0.464000, 49.656384, 0.000000, 0.888448, 0.000000],
[0.508320, 49.690239, 0.000000, 0.885952, 0.000000],
[0.626976, 49.719646, 0.000000, 0.884128, 0.000000],
[0.483872, 49.734207, 0.000000, 0.886592, 0.000000],
[0.409696, 49.695553, 0.000000, 0.883360, 0.000000],
[0.230752, 49.710850, 0.000000, 0.887904, 0.000000],
[0.502496, 49.713951, 0.000000, 0.895808, 0.000000],
[0.274336, 49.797825, 0.000000, 0.888384, 0.000000],
[0.248384, 49.725567, 0.000000, 0.888352, 0.000000],
[0.381920, 49.762402, 0.000000, 0.884320, 0.000000],
[0.264640, 49.661377, 0.000000, 0.877184, 0.000000],
[0.231360, 49.693439, 0.000000, 0.888096, 0.000000],
[0.302176, 49.682495, 0.000000, 0.896992, 0.000000],
[0.468256, 49.683968, 0.000000, 0.885152, 0.000000],
[0.363904, 49.646400, 0.000000, 0.885888, 0.000000],
[0.378720, 49.726177, 0.000000, 0.886752, 0.000000],
[0.417888, 49.671391, 0.000000, 0.886240, 0.000000],
[0.302048, 49.849792, 0.000000, 0.885440, 0.000000],
[0.413664, 49.720512, 0.000000, 0.884448, 0.000000],
[0.414592, 49.801407, 0.000000, 0.884352, 0.000000],
[0.298496, 49.673409, 0.000000, 0.889600, 0.000000],
[0.459648, 49.783455, 0.000000, 0.881376, 0.000000],
[0.403200, 49.673695, 0.000000, 0.882592, 0.000000],
[0.227232, 49.711266, 0.000000, 0.884512, 0.000000],
[0.381920, 49.702560, 0.000000, 0.891200, 0.000000],
[0.399616, 49.675423, 0.000000, 0.885024, 0.000000],
[0.617440, 49.689056, 0.000000, 0.886720, 0.000000],
[0.257216, 49.655041, 0.000000, 0.886080, 0.000000],
[0.480320, 49.671906, 0.000000, 0.886784, 0.000000],
[0.232352, 49.676289, 0.000000, 0.886176, 0.000000],
[0.523808, 49.764545, 0.000000, 0.891488, 0.000000],
[0.429792, 49.874561, 0.000000, 0.891072, 0.000000],
[0.250752, 49.698368, 0.000000, 0.881344, 0.000000],
[0.428224, 49.724609, 0.000000, 0.889760, 0.000000],
[0.322016, 49.710785, 0.000000, 0.900992, 0.000000],
[0.216928, 49.826401, 0.000000, 0.885120, 0.000000],
[0.385696, 49.794655, 0.000000, 0.890016, 0.000000],
[0.464192, 49.701088, 0.000000, 0.884480, 0.000000],
[0.290976, 49.764160, 0.000000, 0.884576, 0.000000],
[0.421632, 49.665855, 0.000000, 0.885088, 0.000000],
[0.273824, 49.778336, 0.000000, 0.891232, 0.000000],
[0.225184, 49.841633, 0.000000, 0.887296, 0.000000],
[0.407616, 49.648224, 0.000000, 0.887808, 0.000000],
[0.381312, 49.740032, 0.000000, 0.885728, 0.000000],
[0.682080, 49.680031, 0.000000, 0.888224, 0.000000],
[0.432288, 49.779808, 0.000000, 0.884992, 0.000000],
[0.278080, 49.816479, 0.000000, 0.886976, 0.000000],
[0.278720, 49.684769, 0.000000, 0.886720, 0.000000],
[0.491936, 49.702591, 0.000000, 0.886016, 0.000000],
[0.441632, 49.701694, 0.000000, 0.886080, 0.000000],
[0.576384, 49.671585, 0.000000, 0.884672, 0.000000],
[0.457408, 49.734367, 0.000000, 0.883104, 0.000000],
[0.466176, 49.655777, 0.000000, 0.885536, 0.000000],
[0.224064, 49.824993, 0.000000, 0.886016, 0.000000],
[0.355840, 49.663265, 0.000000, 0.889504, 0.000000],
[0.534720, 49.680191, 0.000000, 0.885152, 0.000000],
[0.323168, 49.661953, 0.000000, 0.889760, 0.000000],
[0.454144, 49.708321, 0.000000, 0.883360, 0.000000]]

# bbox no backface culling and sorting
p2 = [[0.329984, 98.175964, 0.000000, 0.885632, 0.000000],
[0.270944, 98.230339, 0.000000, 0.885344, 0.000000],
[0.404352, 98.400162, 0.000000, 0.884800, 0.000000],
[0.733536, 98.013794, 0.000000, 0.885728, 0.000000],
[0.491488, 98.053436, 0.000000, 0.886048, 0.000000],
[0.450656, 98.009186, 0.000000, 0.886528, 0.000000],
[0.413280, 98.290337, 0.000000, 0.886656, 0.000000],
[0.223744, 98.431549, 0.000000, 0.886784, 0.000000],
[0.266880, 98.278275, 0.000000, 0.882912, 0.000000],
[0.266784, 98.012924, 0.000000, 0.890144, 0.000000],
[0.224512, 98.200256, 0.000000, 0.885344, 0.000000],
[0.350080, 98.009438, 0.000000, 0.886496, 0.000000],
[0.450624, 98.369247, 0.000000, 0.891008, 0.000000],
[0.348128, 98.340157, 0.000000, 0.886016, 0.000000],
[0.752832, 98.060959, 0.000000, 0.888960, 0.000000],
[0.250400, 98.046402, 0.000000, 0.884352, 0.000000],
[0.223840, 98.175964, 0.000000, 0.887776, 0.000000],
[0.270976, 98.342178, 0.000000, 0.882688, 0.000000],
[0.252160, 98.353821, 0.000000, 0.884000, 0.000000],
[0.640000, 98.022400, 0.000000, 0.885824, 0.000000],
[0.432160, 98.012161, 0.000000, 0.885280, 0.000000],
[0.367872, 98.089981, 0.000000, 0.886240, 0.000000],
[0.328736, 98.169373, 0.000000, 0.886880, 0.000000],
[0.270848, 98.307549, 0.000000, 0.887552, 0.000000],
[0.445984, 98.247742, 0.000000, 0.885728, 0.000000],
[0.361440, 98.069885, 0.000000, 0.887456, 0.000000],
[0.256288, 98.182655, 0.000000, 0.887104, 0.000000],
[0.429408, 98.071106, 0.000000, 0.893472, 0.000000],
[0.226624, 98.313919, 0.000000, 0.886656, 0.000000],
[0.408864, 98.068062, 0.000000, 0.886624, 0.000000],
[0.228192, 98.278114, 0.000000, 0.885568, 0.000000],
[0.405216, 98.055328, 0.000000, 0.886080, 0.000000],
[0.292448, 98.250435, 0.000000, 0.884832, 0.000000],
[0.441792, 98.007904, 0.000000, 0.876832, 0.000000],
[0.390944, 98.112450, 0.000000, 0.882720, 0.000000],
[0.353152, 98.051201, 0.000000, 0.888992, 0.000000],
[0.282848, 98.306717, 0.000000, 0.891360, 0.000000],
[0.661440, 98.017822, 0.000000, 0.883104, 0.000000],
[0.227712, 98.205437, 0.000000, 0.884384, 0.000000],
[0.277600, 98.191231, 0.000000, 0.884320, 0.000000],
[0.219776, 98.228798, 0.000000, 0.883264, 0.000000],
[0.229408, 98.393570, 0.000000, 0.893888, 0.000000],
[0.243680, 98.366692, 0.000000, 0.886816, 0.000000],
[0.417536, 98.045692, 0.000000, 0.887776, 0.000000],
[0.359296, 98.151489, 0.000000, 0.885504, 0.000000],
[0.400224, 98.040092, 0.000000, 0.888224, 0.000000],
[0.287456, 98.199615, 0.000000, 0.884512, 0.000000],
[0.567104, 98.043037, 0.000000, 0.885952, 0.000000],
[0.758208, 98.047325, 0.000000, 0.887936, 0.000000],
[0.302784, 98.051872, 0.000000, 0.887264, 0.000000],
[0.251456, 98.086205, 0.000000, 0.894080, 0.000000],
[0.447872, 98.057854, 0.000000, 0.886688, 0.000000],
[0.442432, 98.223907, 0.000000, 0.886688, 0.000000],
[0.683968, 98.024864, 0.000000, 0.886048, 0.000000],
[0.424928, 98.148605, 0.000000, 0.882208, 0.000000],
[0.689920, 98.088608, 0.000000, 0.891200, 0.000000],
[0.257600, 98.188354, 0.000000, 0.886784, 0.000000],
[0.386112, 98.157982, 0.000000, 0.888000, 0.000000],
[0.520256, 98.264320, 0.000000, 0.884128, 0.000000],
[0.621472, 98.054466, 0.000000, 0.886208, 0.000000],
[0.401856, 98.155357, 0.000000, 0.886272, 0.000000],
[0.406560, 98.068672, 0.000000, 0.887104, 0.000000],
[0.232032, 98.282532, 0.000000, 0.886944, 0.000000],
[0.464864, 98.030403, 0.000000, 0.886400, 0.000000],
[0.431744, 98.085312, 0.000000, 0.889056, 0.000000],
[0.580480, 98.059074, 0.000000, 0.885920, 0.000000],
[0.517152, 98.270721, 0.000000, 0.883840, 0.000000],
[0.418688, 98.052162, 0.000000, 0.888480, 0.000000],
[0.294304, 98.279427, 0.000000, 0.881344, 0.000000],
[0.760256, 98.040611, 0.000000, 0.885120, 0.000000],
[0.319200, 98.050179, 0.000000, 0.883328, 0.000000],
[0.657376, 98.027740, 0.000000, 0.886144, 0.000000],
[0.458912, 98.265823, 0.000000, 0.883584, 0.000000],
[0.791648, 98.080544, 0.000000, 0.888800, 0.000000],
[0.250016, 98.368156, 0.000000, 0.885696, 0.000000]]

# backface culling and sorting but no bbox
p3 = [[0.589248, 110.232414, 0.000000, 0.890784, 0.000000],
[0.820128, 110.080704, 0.000000, 0.886080, 0.000000],
[0.224224, 110.167107, 0.000000, 0.886144, 0.000000],
[0.389888, 110.178268, 0.000000, 0.884608, 0.000000],
[0.432544, 110.082207, 0.000000, 0.888160, 0.000000],
[0.624512, 110.146652, 0.000000, 0.889664, 0.000000],
[0.382784, 110.191841, 0.000000, 0.878848, 0.000000],
[0.378432, 110.137955, 0.000000, 0.887328, 0.000000],
[0.218880, 110.165085, 0.000000, 0.884704, 0.000000],
[0.420736, 110.231583, 0.000000, 0.887264, 0.000000],
[0.322016, 110.105537, 0.000000, 0.887392, 0.000000],
[0.259072, 110.186722, 0.000000, 0.886016, 0.000000],
[0.393024, 110.111328, 0.000000, 0.887136, 0.000000],
[0.477696, 110.208961, 0.000000, 0.880704, 0.000000],
[0.599424, 110.096733, 0.000000, 0.888800, 0.000000],
[0.362240, 110.284988, 0.000000, 0.884864, 0.000000],
[0.791872, 110.098274, 0.000000, 0.892608, 0.000000],
[0.267136, 110.176414, 0.000000, 0.887680, 0.000000],
[0.442496, 110.108383, 0.000000, 0.889632, 0.000000],
[0.479104, 110.171745, 0.000000, 0.887136, 0.000000],
[0.574304, 110.152702, 0.000000, 0.883872, 0.000000],
[0.691936, 110.120605, 0.000000, 0.887328, 0.000000],
[0.493600, 110.149345, 0.000000, 0.889600, 0.000000],
[0.266528, 110.123299, 0.000000, 0.887104, 0.000000],
[0.368992, 110.101982, 0.000000, 0.884384, 0.000000],
[0.440416, 110.067390, 0.000000, 0.886944, 0.000000],
[0.271264, 110.185951, 0.000000, 0.883456, 0.000000],
[0.436800, 110.276413, 0.000000, 0.886272, 0.000000],
[0.302496, 110.155106, 0.000000, 0.886368, 0.000000],
[0.257024, 110.206146, 0.000000, 0.882048, 0.000000],
[0.400128, 110.205406, 0.000000, 0.885888, 0.000000],
[0.405888, 110.163391, 0.000000, 0.881472, 0.000000],
[0.638688, 110.089699, 0.000000, 0.885504, 0.000000],
[0.470112, 110.206688, 0.000000, 0.885696, 0.000000],
[0.364512, 110.144386, 0.000000, 0.887168, 0.000000],
[0.227488, 110.144318, 0.000000, 0.885824, 0.000000],
[0.434336, 110.192352, 0.000000, 0.879872, 0.000000],
[0.394528, 110.098717, 0.000000, 0.890816, 0.000000],
[0.251232, 110.081123, 0.000000, 0.887040, 0.000000],
[0.488832, 110.224220, 0.000000, 0.882912, 0.000000],
[0.324448, 110.215614, 0.000000, 0.890880, 0.000000],
[0.227808, 110.177475, 0.000000, 0.885984, 0.000000],
[0.423936, 110.180511, 0.000000, 0.896864, 0.000000],
[0.418624, 110.190399, 0.000000, 0.887616, 0.000000],
[0.690976, 110.148483, 0.000000, 0.888160, 0.000000],
[0.466336, 110.208099, 0.000000, 0.885728, 0.000000],
[0.439936, 110.162941, 0.000000, 0.888768, 0.000000],
[0.349408, 110.181725, 0.000000, 0.883040, 0.000000],
[0.380320, 110.213631, 0.000000, 0.885888, 0.000000],
[0.287456, 110.208572, 0.000000, 0.887072, 0.000000],
[0.452224, 110.148735, 0.000000, 0.888864, 0.000000],
[0.249024, 110.271683, 0.000000, 0.885184, 0.000000],
[0.390432, 110.211906, 0.000000, 0.886304, 0.000000],
[0.486176, 110.181313, 0.000000, 0.888256, 0.000000],
[0.663424, 110.230049, 0.000000, 0.889312, 0.000000],
[0.893152, 110.279137, 0.000000, 0.897856, 0.000000],
[0.246016, 110.163040, 0.000000, 0.886784, 0.000000],
[0.285120, 110.189697, 0.000000, 0.883328, 0.000000],
[0.411296, 110.238403, 0.000000, 0.890656, 0.000000],
[0.392416, 110.261086, 0.000000, 0.886688, 0.000000],
[0.601216, 110.185822, 0.000000, 0.886560, 0.000000],
[0.472800, 110.222466, 0.000000, 0.884864, 0.000000],
[0.428064, 110.150497, 0.000000, 0.894624, 0.000000],
[0.228096, 110.241440, 0.000000, 0.884992, 0.000000],
[0.421280, 110.091682, 0.000000, 0.887264, 0.000000],
[0.455104, 110.194496, 0.000000, 0.881984, 0.000000],
[0.662464, 110.132545, 0.000000, 0.888544, 0.000000],
[0.464416, 110.161118, 0.000000, 0.873792, 0.000000],
[0.423840, 110.133026, 0.000000, 0.897376, 0.000000],
[0.440672, 110.202019, 0.000000, 0.883840, 0.000000]]

# no backface culling and sorting and no bbox
p4 = [[0.284640, 217.891769, 0.000000, 0.883968, 0.000000],
[0.388032, 217.745468, 0.000000, 0.887232, 0.000000],
[0.294816, 217.824615, 0.000000, 0.885632, 0.000000],
[0.422592, 217.674911, 0.000000, 0.887328, 0.000000],
[0.422464, 217.887451, 0.000000, 0.885664, 0.000000],
[0.601760, 217.805435, 0.000000, 0.885888, 0.000000],
[0.603520, 217.779297, 0.000000, 0.888704, 0.000000],
[0.511616, 217.748322, 0.000000, 0.887008, 0.000000],
[0.285344, 217.957336, 0.000000, 0.881824, 0.000000],
[0.727904, 217.711365, 0.000000, 0.888128, 0.000000],
[0.295712, 217.995422, 0.000000, 0.881024, 0.000000],
[0.225504, 218.031235, 0.000000, 0.887488, 0.000000],
[0.264864, 217.880508, 0.000000, 0.885792, 0.000000],
[0.530752, 217.729187, 0.000000, 0.886336, 0.000000],
[0.227968, 217.940231, 0.000000, 0.885600, 0.000000],
[0.326528, 217.728775, 0.000000, 0.886368, 0.000000],
[0.218624, 217.972412, 0.000000, 0.887040, 0.000000],
[0.313536, 217.947067, 0.000000, 0.886336, 0.000000],
[0.421824, 218.040283, 0.000000, 0.884032, 0.000000],
[0.432672, 217.812546, 0.000000, 0.888352, 0.000000],
[0.225344, 217.911392, 0.000000, 0.887648, 0.000000],
[0.554240, 217.756668, 0.000000, 0.899616, 0.000000],
[0.355904, 218.013824, 0.000000, 0.884480, 0.000000],
[0.625856, 217.788284, 0.000000, 0.886080, 0.000000],
[0.418304, 217.869507, 0.000000, 0.886080, 0.000000],
[0.570592, 217.763168, 0.000000, 0.887296, 0.000000],
[0.342720, 217.886108, 0.000000, 0.886016, 0.000000],
[0.372960, 217.760986, 0.000000, 0.885888, 0.000000],
[0.419712, 217.815720, 0.000000, 0.888000, 0.000000],
[0.252640, 217.765472, 0.000000, 0.886432, 0.000000],
[0.360864, 218.011780, 0.000000, 0.884832, 0.000000],
[0.342240, 217.799835, 0.000000, 0.886720, 0.000000],
[0.226656, 217.896286, 0.000000, 0.885440, 0.000000],
[0.378880, 217.672455, 0.000000, 0.888704, 0.000000],
[0.316736, 217.927002, 0.000000, 0.886080, 0.000000],
[0.612192, 217.807556, 0.000000, 0.887296, 0.000000],
[0.433536, 217.903900, 0.000000, 0.891744, 0.000000],
[0.429984, 217.820953, 0.000000, 0.885664, 0.000000],
[0.220128, 218.021469, 0.000000, 0.886240, 0.000000],
[0.438752, 217.785629, 0.000000, 0.890912, 0.000000],
[0.438528, 218.021820, 0.000000, 0.883168, 0.000000],
[0.308128, 217.730911, 0.000000, 0.885056, 0.000000],
[0.440928, 217.842331, 0.000000, 0.884992, 0.000000],
[0.389504, 217.816833, 0.000000, 0.884544, 0.000000],
[0.294144, 217.949127, 0.000000, 0.885504, 0.000000],
[0.406880, 217.827133, 0.000000, 0.889280, 0.000000],
[0.294112, 217.906876, 0.000000, 0.886944, 0.000000],
[0.300768, 217.738205, 0.000000, 0.886816, 0.000000],
[0.399008, 218.059418, 0.000000, 0.886112, 0.000000],
[0.382624, 217.750778, 0.000000, 0.887424, 0.000000],
[0.225728, 217.918564, 0.000000, 0.883232, 0.000000],
[0.643680, 217.815231, 0.000000, 0.885952, 0.000000],
[0.369632, 217.877625, 0.000000, 0.884864, 0.000000],
[0.613120, 217.810562, 0.000000, 0.887840, 0.000000],
[0.334944, 217.984222, 0.000000, 0.886240, 0.000000],
[0.378912, 217.729919, 0.000000, 0.887584, 0.000000],
[0.300256, 217.944290, 0.000000, 0.884000, 0.000000],
[0.490272, 217.909851, 0.000000, 0.883936, 0.000000],
[0.356192, 217.856613, 0.000000, 0.885312, 0.000000],
[0.706912, 217.638535, 0.000000, 0.888544, 0.000000],
[0.340640, 217.817093, 0.000000, 0.885792, 0.000000],
[0.312480, 217.785767, 0.000000, 0.886912, 0.000000],
[0.310016, 217.851898, 0.000000, 0.885728, 0.000000],
[0.367360, 217.699356, 0.000000, 0.899968, 0.000000],
[0.267520, 217.957657, 0.000000, 0.887232, 0.000000]]

# all optimizations MSAA4x
p5 = [[0.330176, 50.216671, 154.838242, 0.888544, 0.000000],
[0.416480, 49.992256, 154.537628, 0.885536, 0.000000],
[0.260704, 49.866367, 154.463867, 0.892544, 0.000000],
[0.269792, 50.268002, 155.127777, 0.887552, 0.000000],
[0.226304, 49.853951, 154.479172, 0.886432, 0.000000],
[0.479904, 49.918400, 154.396027, 0.885696, 0.000000],
[0.727872, 50.495232, 155.497253, 0.888320, 0.000000],
[0.416192, 49.841854, 154.473511, 0.885568, 0.000000],
[0.477216, 49.798496, 154.661057, 0.887936, 0.000000],
[0.225376, 50.540607, 155.692322, 0.888224, 0.000000],
[0.602464, 49.796032, 154.395004, 0.888352, 0.000000],
[0.296992, 50.284607, 155.099106, 0.887008, 0.000000],
[0.674432, 49.810497, 154.436676, 1.140640, 0.000000],
[0.521856, 50.461887, 155.622406, 0.889888, 0.000000],
[0.679200, 50.278687, 155.100357, 0.887328, 0.000000],
[0.316640, 49.854912, 154.469116, 0.886176, 0.000000],
[0.485344, 50.415455, 155.901413, 0.889664, 0.000000],
[0.416640, 50.242783, 155.539749, 0.886688, 0.000000],
[0.721088, 49.859585, 154.460770, 0.889664, 0.000000],
[0.351008, 49.875935, 154.631943, 0.890912, 0.000000],
[0.419584, 50.248001, 155.653244, 0.886112, 0.000000],
[0.477216, 49.821342, 154.363708, 0.887168, 0.000000],
[0.403104, 50.496159, 155.051193, 0.887360, 0.000000],
[0.222048, 50.446815, 154.484039, 0.885728, 0.000000],
[0.595392, 49.787327, 154.505829, 0.886784, 0.000000],
[0.921312, 49.785183, 154.574844, 0.889696, 0.000000],
[0.559424, 50.810818, 154.590149, 0.884800, 0.000000],
[0.301312, 49.924000, 154.556168, 0.886368, 0.000000],
[0.369376, 50.280670, 155.623672, 0.886048, 0.000000],
[0.425984, 49.821503, 154.374619, 0.885440, 0.000000],
[0.229568, 50.466656, 155.996582, 0.885120, 0.000000],
[0.446048, 49.989506, 154.561722, 0.889824, 0.000000],
[0.592000, 50.494335, 155.382980, 0.884832, 0.000000],
[0.223968, 49.886047, 154.425369, 0.884576, 0.000000],
[0.250048, 50.364704, 154.580765, 0.886112, 0.000000],
[0.413952, 49.898594, 154.724411, 0.887552, 0.000000],
[0.301760, 49.827168, 154.435455, 0.892576, 0.000000],
[0.491488, 50.530239, 154.692825, 0.887904, 0.000000],
[0.641568, 49.823135, 154.480057, 0.892544, 0.000000],
[0.267296, 49.933281, 154.412262, 0.892448, 0.000000],
[0.490560, 50.250656, 155.085831, 0.889984, 0.000000],
[0.428960, 49.877792, 154.565536, 0.883424, 0.000000],
[0.690368, 49.849407, 154.455841, 0.887616, 0.000000],
[0.330976, 50.248608, 155.317978, 0.891584, 0.000000],
[0.499392, 49.775105, 154.465088, 0.887232, 0.000000],
[0.252480, 50.418976, 156.053146, 0.886496, 0.000000],
[0.730112, 50.276928, 155.667877, 0.884128, 0.000000],
[0.440832, 49.859650, 154.622971, 0.891648, 0.000000],
[0.264352, 49.931232, 155.842148, 0.889248, 0.000000],
[0.386848, 50.428577, 155.713821, 0.890528, 0.000000],
[0.219136, 49.926434, 154.511642, 0.884576, 0.000000],
[0.229056, 49.864990, 155.174561, 0.900384, 0.000000],
[0.361824, 50.244034, 156.084091, 0.886560, 0.000000],
[0.310528, 49.921726, 154.592957, 0.892288, 0.000000],
[0.439968, 50.281567, 155.178787, 0.896192, 0.000000],
[0.338432, 50.585728, 154.910400, 0.890496, 0.000000],
[0.517088, 49.868385, 154.561661, 0.884704, 0.000000],
[0.225600, 50.337921, 155.592743, 0.890496, 0.000000],
[0.408832, 50.540222, 155.313477, 0.886112, 0.000000],
[0.457056, 49.856224, 154.611099, 0.887264, 0.000000],
[0.458336, 50.294880, 155.617798, 0.888288, 0.000000],
[0.764896, 50.522945, 155.439041, 0.887200, 0.000000],
[0.261920, 49.808384, 154.604889, 0.887008, 0.000000],
[0.298208, 49.864574, 154.460709, 0.893344, 0.000000],
[0.289408, 50.474014, 155.688995, 0.886400, 0.000000],
[0.305728, 50.442242, 155.235992, 0.890208, 0.000000],
[0.584704, 50.298496, 154.812668, 0.886112, 0.000000]]

# no optimizations MSAA4x
p6 = [[0.320320, 218.566727, 660.388489, 0.896064, 0.000000],
[0.380192, 218.213318, 660.216370, 0.894432, 0.000000],
[0.227904, 218.423264, 659.974548, 0.891296, 0.000000],
[0.419200, 218.241028, 660.166260, 0.891936, 0.000000],
[0.444928, 218.340637, 660.329590, 0.893088, 0.000000],
[0.334656, 218.404709, 660.248047, 0.895232, 0.000000],
[0.493856, 218.518845, 660.270874, 0.897984, 0.000000],
[0.397248, 218.391907, 660.536865, 0.897568, 0.000000],
[0.222144, 218.454971, 660.400391, 0.895744, 0.000000],
[0.464768, 218.434174, 660.274292, 0.891904, 0.000000],
[0.326176, 218.503296, 660.201477, 0.895136, 0.000000],
[0.594976, 218.260193, 660.441650, 0.894560, 0.000000],
[0.374240, 218.528763, 660.428589, 0.896832, 0.000000],
[0.437440, 218.253372, 660.380615, 0.893120, 0.000000],
[0.673280, 218.378265, 660.262024, 0.892672, 0.000000],
[0.570432, 218.258240, 660.261963, 0.895008, 0.000000],
[0.264000, 218.511810, 660.293091, 0.901312, 0.000000],
[0.658688, 218.385498, 660.255310, 0.891584, 0.000000],
[0.341472, 218.508606, 660.451477, 0.890528, 0.000000],
[0.337056, 218.305817, 660.285400, 0.896448, 0.000000],
[0.229312, 218.470367, 660.316589, 0.894272, 0.000000],
[0.281760, 218.409058, 660.113159, 0.891904, 0.000000],
[0.441280, 218.360092, 660.282104, 0.894752, 0.000000],
[0.226432, 218.370087, 660.116394, 0.895808, 0.000000],
[0.379040, 218.347260, 660.239014, 0.895392, 0.000000],
[0.554240, 218.270020, 660.157959, 0.895392, 0.000000],
[0.227584, 218.493958, 660.201843, 0.902976, 0.000000],
[0.492640, 218.449829, 660.314575, 0.893408, 0.000000],
[0.537376, 218.428284, 660.186340, 0.901248, 0.000000],
[0.661504, 218.306244, 660.145264, 0.892320, 0.000000],
[0.251616, 218.484451, 660.609680, 0.894560, 0.000000],
[0.318048, 218.370880, 660.378784, 0.892576, 0.000000],
[0.255168, 218.391266, 660.399231, 0.896000, 0.000000],
[0.224224, 218.348572, 660.299805, 0.896096, 0.000000],
[0.435104, 218.530045, 660.387695, 0.895392, 0.000000],
[0.647136, 218.368134, 660.564941, 0.893856, 0.000000],
[0.311424, 218.473953, 660.288818, 0.894080, 0.000000],
[0.457824, 218.324646, 660.378174, 0.892032, 0.000000],
[0.252512, 218.556610, 660.402710, 0.896736, 0.000000],
[0.388768, 218.317444, 660.241699, 0.893120, 0.000000],
[0.381216, 218.502014, 660.572571, 0.895392, 0.000000],
[0.659616, 218.308609, 660.231506, 0.897088, 0.000000],
[0.492064, 218.474777, 660.388977, 0.894016, 0.000000],
[0.269216, 218.318817, 660.390381, 0.893600, 0.000000],
[0.228320, 218.425537, 660.367493, 0.897344, 0.000000],
[0.413248, 218.266403, 660.223999, 0.893184, 0.000000]]


# all optimization SSAA
p7 = [[0.319936, 200.197723, 0.000000, 3.479488, 0.254752],
[0.261472, 202.024506, 0.000000, 3.476320, 0.255232],
[0.261056, 200.256409, 0.000000, 3.481248, 0.255680],
[0.529088, 200.187805, 0.000000, 3.476736, 0.254784],
[0.399872, 202.294983, 0.000000, 3.475392, 0.255744],
[0.500672, 201.595642, 0.000000, 3.477280, 0.255680],
[0.404352, 200.180130, 0.000000, 3.474528, 0.254240],
[0.294432, 200.282303, 0.000000, 3.471616, 0.254560],
[0.444192, 200.206085, 0.000000, 3.473248, 0.254720],
[0.435456, 201.302887, 0.000000, 3.478208, 0.255712],
[0.572896, 203.124832, 0.000000, 3.472992, 0.255008],
[0.411136, 200.218140, 0.000000, 3.468704, 0.255872],
[0.433536, 200.257828, 0.000000, 3.473600, 0.258688],
[0.259712, 203.637314, 0.000000, 3.480416, 0.254816],
[0.291552, 200.251526, 0.000000, 3.478400, 0.255040],
[0.360640, 200.160263, 0.000000, 3.478336, 0.254880],
[0.308384, 200.221191, 0.000000, 3.475552, 0.254688],
[0.478592, 203.352158, 0.000000, 3.470496, 0.255680],
[0.614560, 200.135559, 0.000000, 3.475520, 0.255040],
[0.296384, 200.305374, 0.000000, 3.475488, 0.253504],
[0.595872, 203.332260, 0.000000, 3.477600, 0.260640],
[0.366592, 200.307205, 0.000000, 3.475264, 0.253952],
[0.659936, 200.277222, 0.000000, 3.473408, 0.254336],
[0.257280, 201.149216, 0.000000, 3.478080, 0.255104],
[0.293536, 203.067459, 0.000000, 3.480448, 0.257440],
[0.326912, 202.290054, 0.000000, 3.477152, 0.253920],
[0.439232, 200.182144, 0.000000, 3.474624, 0.254848],
[0.371776, 203.654846, 0.000000, 3.478560, 0.254976],
[0.669664, 200.221954, 0.000000, 3.479648, 0.255872],
[0.233568, 200.348221, 0.000000, 3.478528, 0.255328],
[0.424544, 200.920319, 0.000000, 3.479264, 0.254272],
[0.224896, 203.114822, 0.000000, 3.476576, 0.255360],
[0.417536, 200.383270, 0.000000, 3.482272, 0.255648],
[0.275104, 201.377625, 0.000000, 3.475648, 0.256064],
[0.599552, 200.262589, 0.000000, 3.480160, 0.256064],
[0.401600, 202.645050, 0.000000, 3.479168, 0.254336],
[0.482400, 200.309433, 0.000000, 3.481536, 0.254752],
[0.228160, 203.721054, 0.000000, 3.474688, 0.254144],
[0.439552, 200.287903, 0.000000, 3.473952, 0.255392],
[0.461280, 202.359741, 0.000000, 3.477536, 0.256352],
[0.702144, 200.332520, 0.000000, 3.474528, 0.254720],
[0.438592, 200.464996, 0.000000, 3.479264, 0.255840],
[0.494496, 202.470169, 0.000000, 3.482112, 0.255200],
[0.420032, 200.366562, 0.000000, 3.475264, 0.254336],
[0.371360, 203.980316, 0.000000, 3.476544, 0.255808],
[0.422496, 200.433182, 0.000000, 3.478816, 0.255136],
[0.271520, 202.048294, 0.000000, 3.475072, 0.255040],
[0.546240, 200.309479, 0.000000, 3.474048, 0.254176],
[0.528032, 203.205338, 0.000000, 3.478528, 0.255648],
[0.439456, 202.599426, 0.000000, 3.473984, 0.254496],
[0.682656, 200.300674, 0.000000, 3.478400, 0.254592],
[0.279936, 200.292480, 0.000000, 3.475712, 0.253888],
[0.573216, 202.630310, 0.000000, 3.476544, 0.254432],
[0.366336, 201.789658, 0.000000, 3.474400, 0.255136],
[0.803392, 200.341858, 0.000000, 3.474400, 0.255680],
[0.227040, 203.064453, 0.000000, 3.476576, 0.255168],
[0.518976, 200.330429, 0.000000, 3.473088, 0.253408],
[0.449344, 201.538300, 0.000000, 3.475680, 0.254912],
[0.258400, 203.756058, 0.000000, 3.475680, 0.254304],
[0.490592, 200.229980, 0.000000, 3.736992, 0.258784],
[0.411328, 201.636993, 0.000000, 3.476960, 0.256608],
[0.229920, 200.371902, 0.000000, 3.474432, 0.254112],
[0.360320, 202.941757, 0.000000, 3.476128, 0.254592],
[0.432800, 202.121216, 0.000000, 3.478656, 0.254816],
[0.595168, 200.272644, 0.000000, 3.477504, 0.254464],
[0.460992, 203.372421, 0.000000, 3.479392, 0.254944],
[0.365344, 200.344955, 0.000000, 3.473120, 0.255264],
[0.678144, 201.549026, 0.000000, 3.476704, 0.255168],
[0.514208, 203.586365, 0.000000, 3.484768, 0.255392],
[0.413376, 203.008865, 0.000000, 3.473376, 0.255776],
[0.582368, 201.979202, 0.000000, 3.477888, 0.254656],
[0.367264, 200.388474, 0.000000, 3.473472, 0.254048],
[0.321664, 203.103836, 0.000000, 3.479488, 0.255296],
[0.223904, 202.339005, 0.000000, 3.477728, 0.254400],
[0.437152, 200.332794, 0.000000, 3.475296, 0.255744],
[0.444480, 203.670013, 0.000000, 3.473984, 0.255680],
[0.730912, 200.287399, 0.000000, 3.472416, 0.254816]]


# no optimizations SSAA
p8 = [[0.339008, 869.142578, 0.000000, 3.440640, 0.252768],
[0.260800, 869.426453, 0.000000, 3.444960, 0.252768],
[0.225216, 869.487915, 0.000000, 3.440736, 0.253024],
[0.390176, 869.082886, 0.000000, 3.443520, 0.253984],
[0.418048, 869.484680, 0.000000, 3.438656, 0.253408],
[0.635456, 869.182556, 0.000000, 3.443904, 0.252800],
[0.260800, 869.479919, 0.000000, 3.442816, 0.252992],
[0.373888, 869.219116, 0.000000, 3.444096, 0.257920],
[0.232128, 869.142883, 0.000000, 3.440992, 0.252480],
[0.231968, 869.217102, 0.000000, 3.441120, 0.253184],
[0.448384, 869.239868, 0.000000, 3.440096, 0.252160],
[0.257088, 869.053955, 0.000000, 3.446432, 0.255552],
[0.221184, 869.248901, 0.000000, 3.438816, 0.252544],
[0.296160, 869.316956, 0.000000, 3.445440, 0.251392],
[0.326528, 869.232605, 0.000000, 3.440448, 0.255168],
[0.398048, 869.016174, 0.000000, 3.444032, 0.253504],
[0.470176, 869.163818, 0.000000, 3.437984, 0.253152],
[0.244544, 869.090820, 0.000000, 3.445248, 0.251328],
[0.507328, 869.353027, 0.000000, 3.440672, 0.251872],
[0.724928, 869.088562, 0.000000, 3.444768, 0.253440],
[0.247552, 869.197815, 0.000000, 3.436768, 0.252352],
[0.389824, 869.120911, 0.000000, 3.437536, 0.250912],
[0.467136, 869.173096, 0.000000, 3.447200, 0.252768],
[0.660992, 868.958923, 0.000000, 3.448800, 0.252384],
[0.444160, 869.207092, 0.000000, 3.442368, 0.251936],
[0.367200, 869.233765, 0.000000, 3.442880, 0.253248],
[0.307744, 869.647766, 0.000000, 3.442336, 0.252448],
[0.472928, 869.365356, 0.000000, 3.443936, 0.252192],
[0.449248, 869.312134, 0.000000, 3.442144, 0.252992],
[0.568896, 869.215515, 0.000000, 3.439808, 0.254464],
[0.223360, 869.474548, 0.000000, 3.446624, 0.253824],
[0.422176, 869.053894, 0.000000, 3.446112, 0.254304],
[0.248576, 869.274719, 0.000000, 3.436352, 0.251744],
[0.500192, 869.180725, 0.000000, 3.445120, 0.252576],
[0.465664, 869.346008, 0.000000, 3.441088, 0.252032],
[0.307552, 869.191345, 0.000000, 3.440640, 0.254752],
[0.422752, 869.463501, 0.000000, 3.439872, 0.253504],
[0.472000, 869.236145, 0.000000, 3.446400, 0.252896],
[0.267840, 869.141968, 0.000000, 3.447360, 0.252608],
[0.391008, 869.072083, 0.000000, 3.446240, 0.251968],
[0.403168, 869.467285, 0.000000, 3.438528, 0.252320],
[0.661120, 869.138489, 0.000000, 3.449440, 0.253696],
[0.437984, 869.180115, 0.000000, 3.442688, 0.253184],
[0.399968, 869.233276, 0.000000, 3.447840, 0.254304],
[0.301600, 869.605347, 0.000000, 3.446144, 0.252416],
[0.681792, 869.258362, 0.000000, 3.445792, 0.254592],
[0.362496, 869.286743, 0.000000, 3.441760, 0.253088]]



# averages:
pp1 = np.sum(np.array(p1), axis = 0) / len(p1)
pp2 = np.sum(np.array(p2), axis = 0) / len(p2)
pp3 = np.sum(np.array(p3), axis = 0) / len(p3) 
pp4 = np.sum(np.array(p4), axis = 0) / len(p4)
pp5 = np.sum(np.array(p5), axis = 0) / len(p5)
pp6 = np.sum(np.array(p6), axis = 0) / len(p6)
pp7 = np.sum(np.array(p7), axis = 0) / len(p7)
pp8 = np.sum(np.array(p8), axis = 0) / len(p8)

print pp1
print pp2
print pp3
print pp4
print pp5
print pp6
print pp7
print pp8





# Data to plot
labels = ['vertexTandA', 'scanline', 'aa', 'render', 'downsample']
colors = ['#005511', '#002244', '#004477', '#118899', '#990000']
explode = (0.1, 0.5, 0.2, 0.1, 0.3)


P = [pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8]
titles = ['optimized\nfunctions time percentage', 
          'aabb only\nfunctions time percentage', 
          'backface cull\nfunctions time percentage', 
          'no opt\nfunctions time percentage',
          'MSAA 4x opt\nfunctions time percentage',
          'MSAA4x no opt\nfunctions time percentage',
          'SSAA opt\nfunctions time percentage',
          'SSAA no opt\nfunctions time percentage']


for i in range(8):
    sizes = P[i]
    
    percent = 100.*P[i]/P[i].sum()

    print percent

    # Plot
    fig = plt.figure(facecolor='black')
    #fig.patch.set_alpha(1.0)
    fig.patch.set_facecolor('black')
    plt.rcParams['text.color'] = 'gray'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['lines.linewidth'] = 4

    ax = plt.subplot(111, axisbg='black')
    
    pie = ax.pie(sizes, explode=explode, colors=colors, textprops = {'color':'#aaaaaa', 'fontweight':'bold'},
            autopct='%1.1f%%', shadow=True, startangle=140)



    ax.set_ylabel('Test Benchmark Averages', color = '#338888', fontweight='bold')
    ax.set_title(titles[i])
    ax.patch.set_facecolor('black') 
    ax.axis('equal')

    percentlabels = list(labels)
    for j in range(len(percentlabels)):
        percentlabels[j] += (' %.1f' % percent[j])+'''%'''

    plt.legend(pie[0], percentlabels, loc='upper corner')

    plt.savefig('piechart_%d.png' % i, bbox_inches='tight', facecolor='black')
    #plt.show()
    




fig = plt.figure(facecolor='black')
#fig.patch.set_alpha(1.0)
fig.patch.set_facecolor('black')
plt.rcParams['text.color'] = 'gray'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['lines.linewidth'] = 4

N = 8
t1 = [pp1[0], pp2[0], pp3[0], pp4[0], pp5[0], pp6[0], pp7[0], pp8[0]]
t2 = [pp1[1], pp2[1], pp3[1], pp4[1], pp5[1], pp6[1], pp7[1], pp8[1]]
t3 = [pp1[2], pp2[2], pp3[2], pp4[2], pp5[2], pp6[2], pp7[2], pp8[2]]
t4 = [pp1[3], pp2[3], pp3[3], pp4[3], pp5[3], pp6[3], pp7[3], pp8[3]]
t5 = [pp1[4], pp2[4], pp3[4], pp4[4], pp5[4], pp6[4], pp7[4], pp8[4]]

ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

pl1 = plt.bar(ind, t1, width, color='#004466')
pl2 = plt.bar(ind, t2, width, color='#006699', bottom=t1 )
pl3 = plt.bar(ind, t3, width, color='#11aa88', bottom=t2 )
pl4 = plt.bar(ind, t4, width, color='#ff5555', bottom=t3 )
pl5 = plt.bar(ind, t5, width, color='#00ffaa', bottom=t4 )
pl6 = plt.bar(ind, t5, width, color='#11ff55', bottom=t5 )
pl7 = plt.bar(ind, t5, width, color='#3322ff', bottom=t5 )
pl8 = plt.bar(ind, t5, width, color='#338822', bottom=t5 )

plt.ylabel('Time in ms', color = '#338888', fontweight='bold')
plt.title('Optimization and post processing benchmark')
plt.xticks(ind + width/2., ('optimized', 
                            'aabb\nonly', 
                            'backface\ncull', 
                            'no opt',
                            'MSAA 4x\nopt',
                            'MSAA4x\nno opt',
                            'SSAA\nopt',
                            'SSAA\nno opt'),
            color = '#333333',
            fontweight='bold')

plt.yticks(np.arange(0, 1000, 100), color = '#333333', fontweight='bold')
plt.legend([pl1[0], pl2[0], pl3[0], pl4[0], pl5[0]], labels, loc=0)

plt.savefig('boxchart.png', bbox_inches='tight', facecolor='black')
#plt.show()





# no scanline





