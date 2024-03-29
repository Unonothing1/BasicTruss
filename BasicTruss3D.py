import openseespy.opensees as op

# =============================================================================
# Units
# =============================================================================

m = 1 
N = 1 
Pa= 1

inches = 0.0254*m 
ft = 12*inches
kip = 4.45*10**3*N
Ksi = 6.89*10**6*Pa 


# =============================================================================
# Input Variables
# =============================================================================

x1 = 0.
y1 = 0.

x2 = 20.*ft
y2 = 0.

x3 = 14.*ft
y3 = 0.

x4 = 10.*ft
y4 = 8.*ft

A1 = 10.*inches**2
A2 = 5*inches**2

E = 3000*Ksi

Px = 1000*kip
Py = -50*kip



# =============================================================================
# OpenSees Analysis
# =============================================================================


# remove existing model
op.wipe()

# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 3)
#ndm=	spatial dimension of problem (1,2, or 3)

# define materials
op.uniaxialMaterial("Elastic", 1, E)

# create nodes
op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)
op.node(4, x4, y4)


# set boundary condition
op.fix(1, 1, 1, 1)
op.fix(2, 1, 1, 1)
op.fix(3, 1, 1, 1)
op.fix(4, 0, 0, 1)

# define elements
# op.element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
op.element("Truss", 1, 1, 4, A1, 1)
op.element("Truss", 2, 2, 4, A2, 1)
op.element("Truss", 3, 3, 4, A2, 1)


# create TimeSeries
op.timeSeries("Linear", 1)

# create a plain load pattern
op.pattern("Plain", 1, 1)

# Create the nodal load - command: load nodeID xForce yForce
op.load(4, Px, Py, 0.)


# Record Results
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 4, '-dof', 1,2,3,'disp')
op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2,3, '-dof', 1,2,3,'reaction')
op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2,3, 'forces')


# create SOE
op.system("BandSPD")
# create DOF number
op.numberer("RCM")
# create constraint handler
op.constraints("Plain")

# create integrator
op.integrator("LoadControl", 1.0)

# create algorithm
op.algorithm("Newton")

# create analysis object
op.analysis("Static")

# perform the analysis
op.initialize() 


ok = op.analyze(1)


op.wipe()




# =============================================================================
# OpenSees Analysis
# =============================================================================


# remove existing model
op.wipe()

# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 3)

# define materials
op.uniaxialMaterial("Elastic", 1, E)

# create nodes
op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)
op.node(4, x4, y4)


# set boundary condition
op.fix(1, 1, 1, 1)
op.fix(2, 1, 1, 1)
op.fix(3, 1, 1, 1)
op.fix(4, 0, 0, 1)

# define elements
# op.element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
op.element("Truss", 1, 1, 4, A1, 1)
op.element("Truss", 2, 2, 4, A2, 1)
op.element("Truss", 3, 3, 4, A2, 1)


# create TimeSeries
op.timeSeries("Linear", 1)

# create a plain load pattern
op.pattern("Plain", 1, 1)

# Create the nodal load - command: load nodeID xForce yForce
op.load(4, 0, Py, 0.)


# Record Results
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 4, '-dof', 1,2,3,'disp')
op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2,3, '-dof', 1,2,3,'reaction')
op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2,3, 'forces')


# create SOE
op.system("BandSPD")
# create DOF number
op.numberer("RCM")
# create constraint handler
op.constraints("Plain")
# create integrator`
op.integrator("LoadControl", 1.0)
# create algorithm
op.algorithm("Newton")
# create analysis object
op.analysis("Static")

# perform the analysis

ok=op.analyze(1)

op.wipe()