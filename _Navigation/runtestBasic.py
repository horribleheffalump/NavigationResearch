from BasicModel.AUV import *
from BasicModel.TestEnvironment import *
from Utils.SlopeApproximator import *
from Seabed.Profile import *

np.random.seed(2213123)

#### !!!!! AUV is now a parameter of testenvironment constructor, so it has to be defined before its call

pc=28.0
pr=20.0
tr=20.0


T = 60.0
delta = 1.0
NBeams = 10
accuracy = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
PhiBounds =     [[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr],[pc-pr,pc+pr]]
ThetaBounds =   [[10.0+tr,10.0-tr],   [100.0+tr,100.0-tr],  [190.0+tr,190.0-tr],  [280.0+tr,280.0-tr], [55.0+tr,55.0-tr],   [145.0+tr,145.0-tr],  [235.0+tr,235.0-tr],  [325.0+tr,325.0-tr]]

## for X
#accuracy = [0.1]
#PhiBounds =     [[pc-pr,pc+pr]] 8 + i * 4
#ThetaBounds =   [[100.0+tr,100.0-tr]] 80 + k * 4

## for Y
#accuracy = [0.1]
#PhiBounds =     [[pc-pr,pc+pr]]
#ThetaBounds =   [[280.0+tr,280.0-tr]] 260 + k * 4

## for Z
#accuracy = [0.1]
#PhiBounds =     [[pc-pr,pc+pr]]
#ThetaBounds =   [[190.0+tr,190.0-tr]] 170 + k * 4


#X0 = [0.001,-0.0002,-10.0003]
#V = lambda t: np.array([1.0 + 0.2 * np.cos(1.0 * t), np.cos(0.1 * t), 0.1 * np.sin(2.0 * t)])
#V = lambda t: np.array([0.5, 0.5 * np.cos(0.2 * t), 0.02 * np.sin(0.5 * t)])
#X0 = [10.0, 10.0, -10.0]
#V = lambda t: np.array([0.3, 0.3, -0.02 * np.cos(0.1 * t)])
estimateslope = False 
seabed = Profile()

#X0 = [0.001 + 0.1 * np.random.normal(0,1),-0.0002 + 0.1 * np.random.normal(0,1),-10.0003 + 0.1 * np.random.normal(0,1)]
#V = lambda t: np.array([0.5, 0.5 * np.cos(np.random.normal(0,1) * t), 0.02 * np.sin(np.random.normal(0,1) * t)])
#auv = AUV(X0, V, delta)
#test = testenvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, auv, seabed, estimateslope)
#test.plot3Dtrajectory([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\')
#test.plotspeed([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\')
#test.plotspeederror([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\')

#test.showscheme()

# statistics for position estimation in specified time instants
#for i in range(0,10):
#   test = testenvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, X0, V, seabed, estimateslope)
#   test.stats([20, 40, 80, 159], [1, 3, 2], 'D:\\projects.git\\NavigationResearch\\results\\')


# statistics for speed estimation
#for i in range(0,5000):
#    X0 = [0.001 + 0.1 * np.random.normal(0,1),-0.0002 + 0.1 * np.random.normal(0,1),-10.0003 + 0.1 * np.random.normal(0,1)]
#    vx = np.random.uniform(-1.0,1.0)
#    vyc = np.random.normal(0,1)
#    vzc = np.random.normal(0,1)
#    V = lambda t: np.array([vx, 0.5 * np.cos(vyc * t), 0.02 * np.sin(vzc * t)])
#    print('');
#    print('sample ' + str(i));
#    print('');
#    #np.random.seed(2213123-i*100)
#    estimateslope = False 
#    seabed = Seabed()
#    test = testenvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, X0, V, seabed, estimateslope)
#    test.speedstats([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_known\\')

#    estimateslope = True 
#    seabed = Seabed()
#    test = testenvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, X0, V, seabed, estimateslope)
#    test.speedstats([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_unknown\\')


# single random trajectory
X0 = [0.001 + 0.1 * np.random.normal(0,1),-0.0002 + 0.1 * np.random.normal(0,1),-10.0003 + 0.1 * np.random.normal(0,1)]
vx = np.random.uniform(-1.0,1.0)
vyc = np.random.normal(0,1)
vzc = np.random.normal(0,1)
V = lambda t: np.array([vx, 0.5 * np.cos(vyc * t), 0.02 * np.sin(vzc * t)])
auv = AUV(X0, V, delta)
seabed = Profile()
estimateslope = False 
test = TestEnvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, auv, seabed, estimateslope)
test.run()
test.plotspeed([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_known\\')
test.plot3Dtrajectory([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_known\\')
test.plottrajectory('D:\\projects.git\\NavigationResearch\\results\\slope_known\\')
estimateslope = True 
test = TestEnvironment(T, delta, NBeams, accuracy, PhiBounds, ThetaBounds, auv, seabed, estimateslope)
test.run()
test.plotspeed([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_unknown\\')
test.plot3Dtrajectory([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\slope_unknown\\')
test.plottrajectory('D:\\projects.git\\NavigationResearch\\results\\slope_unknown\\')

#test.showradar([6])
#test.plot3Dtrajectory([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\')
#test.plotspeed([6,6,6], 'D:\\projects.git\\NavigationResearch\\results\\')
#test.plottrajectory3Dseabed()
#test.plottrajectory('D:\\projects.git\\NavigationResearch\\results\\')
#test.plotseabedsequence('D:\\projects.git\\NavigationResearch\\results\\', 'both')
#test.crit()

