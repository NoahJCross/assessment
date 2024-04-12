from Graph import *
from RoutePlanner import RoutePlanner
from Node import Node
from Path import Path


# Defining a dictionary representing the locations and their corresponding nodes and paths
location_map = UndirectedGraph(dict(
    Waurn_Ponds_Estate=Node((-38.20039, 144.29149), dict(intersection3=Path(194, True, False))),
    Deakin_University_Chapel=Node((-38.19889, 144.29623), dict(intersection39=Path(12))),
    Deakin_Library_Waurn_Ponds=Node((-38.19788, 144.29728), dict(intersection40=Path(67))),
    Athletic_Field=Node((-38.19749, 144.30009), dict(intersection42=Path(63), intersection41=Path(35))),
    Deakin_University_Medical_School=Node((-38.19699, 144.29847), dict(intersection27=Path(37))),
    School_of_Engineering=Node((-38.19677, 144.2966), dict(intersection38=Path(47))),
    Parinton_Advanced_Engineering=Node((-38.19504, 144.29274), dict(intersection18=Path(208))),
    Car_Park_20=Node((-38.19418, 144.29395), dict(gradientMarker11=Path(36), intersection26=Path(56))),
    Car_Park_11=Node((-38.19437, 144.29532), dict(intersection26=Path(66), intersection10=Path(48))),
    IISRI=Node((-38.1955, 144.2935), dict(intersection44=Path(13))),
    Deakin_Residential_Services=Node((-38.20066, 144.30259), dict(intersection13=Path(119), gradientMarker27=Path(150))),
    Deakin_University_Geelong_Mosque=Node((-38.19968, 144.29638), dict(intersection6=Path(59, True), gradientMarker35=Path(62, is_paved=False))),
    Deakin_Waurn_Ponds_Shuttle_Service=Node((-38.19844, 144.29835), dict(intersection31=Path(40))),
    Park_and_Go_Free_parking=Node((-38.20068, 144.29509), dict(gradientMarker6=Path(51), intersection6=Path(220))),
    Deakin_Baseball_Club=Node((-38.19613, 144.30356), dict(intersection43=Path(31))),
    Natural_1_Cafe=Node((-38.19692, 144.29525), dict(intersection35=Path(61), intersection1=Path(65))),
    Carbon_Nexus=Node((-38.19613, 144.2924), dict(intersection37=Path(42))),
    Anam_Cara_House_Geelong=Node((-38.20149, 144.29752), dict(intersection15=Path(58))),
    Peter_Thwaites_Lecture_Theater=Node((-38.1987, 144.2983), dict(intersection31=Path(30))),
    Kids_Plus_Foundation=Node((-38.1949, 144.29897), dict(intersection9=Path(131))),
    Car_Park_1=Node((-38.19626, 144.29907), dict(intersection9=Path(117), gradientMarker37=Path(74))),
    Car_Park_16=Node((-38.2004, 144.2983), dict(intersection4=Path(85))),
    BNNT_Technology_Limited=Node((-38.19661, 144.29021), dict(intersection33=Path(152))),
    Epworth_Geelong_Hospital=Node((-38.19386, 144.30252), dict(intersection2=Path(336))),
    Quickstep_Applied_Composites=Node((-38.19566, 144.2966), dict(intersection46=Path(75))),
    intersection1=Node((-38.19662, 144.2946), dict(intersection34=Path(139), intersection23=Path(116))),
    intersection2=Node((-38.19544, 144.2997), dict(gradientMarker36=Path(72), intersection28=Path(128))),
    intersection3=Node((-38.20043, 144.29362), dict(gradientMarker5=Path(29, True, False), gradientMarker6=Path(94, True, False), intersection21=Path(147, True, False))),
    intersection4=Node((-38.19983, 144.29811), dict(intersection6=Path(135), gradientMarker29=Path(73), intersection17=Path(303))),
    intersection5=Node((-38.1986, 144.29885), dict(intersection31=Path(19), gradientMarker31=Path(296), intersection7=Path(85))),
    intersection6=Node((-38.20003, 144.29659), {}),
    intersection7=Node((-38.19799, 144.29886), dict(intersection22=Path(71), intersection41=Path(118), intersection27=Path(99))),
    intersection8=Node((-38.19653, 144.30389), dict(intersection41=Path(383), intersection43=Path(99), gradientMarker15=Path(43), gradientMarker24=Path(114, True, False))),
    intersection9=Node((-38.19565, 144.29843), dict(gradientMarker36=Path(53, True), intersection36=Path(160))),
    intersection10=Node((-38.19448, 144.29585), dict(intersection25=Path(27, True))),
    intersection11=Node((-38.19684, 144.29167), dict(gradientMarker8=Path(127, is_paved=False), gradientMarker10=Path(132, is_paved=False), intersection33=Path(14, True))),
    intersection12=Node((-38.1997, 144.30274), dict(intersection13=Path(24), gradientMarker32=Path(139), intersection29=Path(161))),
    intersection13=Node((-38.19967, 144.30247), dict(intersection17=Path(151))),
    intersection14=Node((-38.20133, 144.29371), dict(gradientMarker5=Path(79, is_paved=False), gradientMarker7=Path(417, is_paved=False), intersection15=Path(297, is_paved=False))),
    intersection15=Node((-38.20173, 144.29697), dict(intersection14=Path(297), gradientMarker4=Path(153, is_paved=False))),
    intersection16=Node((-38.19926, 144.29029), dict(gradientMarker7=Path(103, True, False), gradientMarker14=Path(153, is_paved=False), gradientMarker8=Path(291, True, False))),
    intersection17=Node((-38.19918, 144.30098), dict(gradientMarker30=Path(198))),
    intersection18=Node((-38.19569, 144.29321), dict(intersection34=Path(71), intersection23=Path(197, True), intersection44=Path(28, True))),
    intersection19=Node((-38.19903, 144.29534), dict(intersection21=Path(99), gradientMarker35=Path(99), intersection20=Path(12))),
    intersection20=Node((-38.19892, 144.29536), dict(intersection39=Path(78), gradientMarker34=Path(83, True), gradientMarker9=Path(103, is_paved=False))),
    intersection21=Node((-38.19923, 144.29427), dict(gradientMarker13=Path(114, is_paved=False))),
    intersection22=Node((-38.19798, 144.29807), dict(intersection39=Path(241), intersection40=Path(21))),
    intersection23=Node((-38.19579, 144.29541), dict(intersection24=Path(38))),
    intersection24=Node((-38.19592, 144.29582), dict(intersection46=Path(17), intersection38=Path(85), intersection25=Path(136, True))),
    intersection25=Node((-38.19472, 144.29581), dict(gradientMarker12=Path(111, True))),
    intersection26=Node((-38.19423, 144.29458), dict(gradientMarker12=Path(33, True))),
    intersection27=Node((-38.19714, 144.29869), dict(intersection45=Path(18), intersection40=Path(127), intersection42=Path(108))),
    intersection28=Node((-38.19547, 144.30097), dict(gradientMarker19=Path(47, True), gradientMarker16=Path(203))),
    intersection29=Node((-38.1997, 144.30443), dict(intersection30=Path(101, True, False), gradientMarker25=Path(67, is_paved=False))),
    intersection30=Node((-38.2006, 144.30433), dict(gradientMarker1=Path(137, is_paved=False), gradientMarker26=Path(57))),
    intersection31=Node((-38.19863, 144.29864), dict(gradientMarker28=Path(43, True), gradientMarker30=Path(21, True))),
    intersection32=Node((-38.19861, 144.30425), dict(gradientMarker33=Path(146, True), gradientMarker25=Path(57, True, False), gradientMarker24=Path(140, is_paved=False))),
    intersection33=Node((-38.19674, 144.29158), dict(intersection37=Path(90))),
    intersection34=Node((-38.19623, 144.29325), dict(intersection37=Path(72))),
    intersection35=Node((-38.19717, 144.29588), dict(intersection38=Path(73), gradientMarker34=Path(118))),
    intersection36=Node((-38.196, 144.29672), dict(intersection46=Path(63), intersection38=Path(93))),
    intersection37=Node((-38.1965, 144.29255), {}),
    intersection38=Node((-38.19655, 144.29614), {}),
    intersection39=Node((-38.19878, 144.2962), {}),
    intersection40=Node((-38.19779, 144.29803), {}),
    intersection41=Node((-38.19779, 144.30021), {}),
    intersection42=Node((-38.19695, 144.29987), dict(gradientMarker17=Path(53))),
    intersection43=Node((-38.19586, 144.30355), dict(gradientMarker18=Path(247))),
    intersection44=Node((-38.19547, 144.29335), dict(gradientMarker11=Path(136, True))),
    intersection45=Node((-38.19704, 144.29878), dict(gradientMarker37=Path(53, True), gradientMarker23=Path(114))),
    intersection46=Node((-38.19595, 144.29601), {}),
    gradientMarker1=Node((-38.20138, 144.30336), dict(gradientMarker2=Path(178, True, False))),
    gradientMarker2=Node((-38.2017, 144.30141), dict(gradientMarker3=Path(172, is_paved=False))),
    gradientMarker3=Node((-38.2017, 144.29966), dict(gradientMarker4=Path(86, True, False))),
    gradientMarker4=Node((-38.20169, 144.29867), {}),
    gradientMarker5=Node((-38.20065, 144.29346), {}),
    gradientMarker6=Node((-38.20037, 144.29466), {}),
    gradientMarker7=Node((-38.20013, 144.28996), {}),
    gradientMarker8=Node((-38.1975, 144.29069), {}),
    gradientMarker9=Node((-38.19832, 144.29455), dict(gradientMarker10=Path(196, True, False))),
    gradientMarker10=Node((-38.19724, 144.29305), {}),
    gradientMarker11=Node((-38.19427, 144.29355), {}),
    gradientMarker12=Node((-38.19454, 144.29457), {}),
    gradientMarker13=Node((-38.19925, 144.29297), dict(gradientMarker14=Path(98, True, False))),
    gradientMarker14=Node((-38.19926, 144.29185), {}),
    gradientMarker15=Node((-38.19615, 144.30395), dict(gradientMarker16=Path(105, True))),
    gradientMarker16=Node((-38.19548, 144.30328), {}),
    gradientMarker17=Node((-38.19685, 144.30046), dict(gradientMarker18=Path(65, True))),
    gradientMarker18=Node((-38.19652, 144.30097), {}),
    gradientMarker19=Node((-38.19572, 144.30056), dict(gradientMarker20=Path(36))),
    gradientMarker20=Node((-38.19587, 144.30021), dict(gradientMarker21=Path(35, True))),
    gradientMarker21=Node((-38.19614, 144.30006), dict(gradientMarker22=Path(31))),
    gradientMarker22=Node((-38.1964, 144.30001), dict(gradientMarker23=Path(22, True))),
    gradientMarker23=Node((-38.19656, 144.29987), {}),
    gradientMarker24=Node((-38.19738, 144.30419), {}),
    gradientMarker25=Node((-38.19911, 144.3044), {}),
    gradientMarker26=Node((-38.20031, 144.30381), dict(gradientMarker27=Path(38, True))),
    gradientMarker27=Node((-38.2001, 144.30347), {}),
    gradientMarker28=Node((-38.19901, 144.29868), {}),
    gradientMarker29=Node((-38.1993, 144.29845), {}),
    gradientMarker30=Node((-38.19871, 144.29886), {}),
    gradientMarker31=Node((-38.19833, 144.30221), {}),
    gradientMarker32=Node((-38.19855, 144.30232), {}),
    gradientMarker33=Node((-38.19836, 144.30268), {}),
    gradientMarker34=Node((-38.1982, 144.29556), {}),
    gradientMarker35=Node((-38.1997, 144.29582), {}),
    gradientMarker36=Node((-38.19551, 144.29889), {}),
    gradientMarker37=Node((-38.19686, 144.29874), {})
))

# Creating a RoutePlanner object with start and destination locations and the location map graph
graph_problem = RoutePlanner(
    startLocation="intersection33",
    desiredDestination="gradientMarker2",
    graph=location_map
)


# Finding the shortest path using A* search algorithm
path = graph_problem.a_star_search()


print("Path:", path)


# Function to run A* search for all possible start and destination locations in the given graph
# def run_a_star_for_all_locations(graph):
#     for start_location in graph.nodes.keys():
#         for destination in graph.nodes.keys():
#             if start_location != destination:
#                 graph_problem = GraphProblem(
#                     startLocation=start_location,
#                     desiredDestination=destination,
#                     graph=graph
#                 )
#                 graph_problem.comparison_data()

# run_a_star_for_all_locations(location_map)