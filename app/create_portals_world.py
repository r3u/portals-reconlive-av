#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from db import db
from model import World, Location, Path, Session, LocationInfo


def add(obj):
    db.session.add(obj)
    return obj


def create_test_world():
    world = add(World(name='pOrtals::reconLIVE:AudioTest'))

    # Transient zones
    fromPortal = add(Location(name='pOrtal', world=world))
    oceanSurface = add(Location(name='Ocean Surface', world=world))

    # Ocean zone
    oceanFloor = add(Location(name='Ocean Floor', world=world))
    oceanPortal = add(Location(name='pOrtal area', world=world))

    # Tower zone
    towerTop = add(Location(name='Tower Top', world=world))
    towerStairway = add(Location(name='Stairway', world=world))
    towerBase = add(Location(name='Base of the Tower', world=world))

    # Secret Island abbr. SI
    siSurface = add(Location(name='SI Surface', world=world))
    siSafeHouse = add(Location(name='SI Safe House', world=world))

    # Sunshine plaza (prev. sunrise/sunset) abbr. SP
    spBeach = add(Location(name='SP Beach', world=world))
    spBeachToClearing = add(Location(name='SP Forest Path B', world=world))
    spRockPool = add(Location(name='SP Rock Pool', world=world))
    spForest = add(Location(name='SP Forest', world=world))
    spCaveMouth = add(Location(name='SP Cave Mouth', world=world))
    spCave = add(Location(name='SP Cave', world=world))
    spTikiPool = add(Location(name='SP Tiki Pool', world=world))
    spTikiBar = add(Location(name='SP Tiki Hut Bar', world=world))
    spTikiBasement = add(Location(name='SP Bar Basement', world=world))
    spTikiPoolToClearing = add(Location(name='SP Forest Path TP', world=world))
    spHarbour = add(Location(name='SP Harbour', world=world))
    spHarbourToClearing = add(Location(name='SP Forest Path H', world=world))
    spMaze = add(Location(name='SP Maze', world=world))
    spClearing = add(Location(name='SP Hotel Clearing', world=world))

    # Pink Lake Island abbr. PLI
    pliLanding = add(Location(name='PLI Landing', world=world))
    pliBoathouseBay = add(Location(name='PLI Boathouse Bay ', world=world))
    pliBoathouse = add(Location(name='PLI Boathouse', world=world))
    pliIsolatedBeach = add(Location(name='Isolated Beach', world=world))
    pliRavine = add(Location(name='PLI Ravine', world=world))
    pliRavineCave = add(Location(name='PLI Ravine Cave', world=world))
    pliRavineToBrooke_right = add(Location(name='PLI Brooke (right fork)', world=world))
    pliRavineToBrooke_Left = add(Location(name='PLI Brooke (left fork)', world=world))
    pliLostForest = add(Location(name='PLI Lost Forest', world=world))
    pliOldTree = add(Location(name='PLI Old Tree', world=world))
    pliInsideOldTree = add(Location(name='PLI Tree Tunnel', world=world))
    pliFallingLog = add(Location(name='PLI Falling Log', world=world))
    pliMonMtSlope = add(Location(name='PLI Monument Mt. Slope', world=world))
    pliMonMtPeak = add(Location(name='PLI Monument Mt. Peak', world=world))
    pliNorthShore = add(Location(name='PLI Lake - North Shore', world=world))
    pliSouthShore = add(Location(name='PLI Lake - South Shore', world=world))
    pliLakeCabin = add(Location(name='PLI Cabin on the Lake', world=world))
    pliRiseCabin = add(Location(name='PLI Cabin on the Rise', world=world))
    pliSkiMtSlopeN = add(Location(name='PLI Ski Mt. Slope - North', world=world))
    pliSkiMtSlopeS = add(Location(name='PLI Ski Mt. Slope - South', world=world))
    pliSkiMtPeak = add(Location(name='PLI Ski Mt. Peak', world=world))
    pliRestCabinRm1 = add(Location(name='PLI Rest Cabin - Main space', world=world))
    pliRestCabinRm2 = add(Location(name='PLI Rest Cabin - Bedroom', world=world))
    pliBarn = add(Location(name='PLI Barn', world=world))
    pliSkiLiftTop = add(Location(name='PLI Ski Lift Controls - Top', world=world))
    pliHeliPad = add(Location(name='PLI Helicopter Pad', world=world))
    pliSkiLiftClearing = add(Location(name='PLI Ski Lift Clearing', world=world))
    pliSkiLiftBottom = add(Location(name='PLI Ski Lift Controls - Bottom', world=world))
    pliPass = add(Location(name='PLI The Pass', world=world))
    pliCliffCave = add(Location(name='PLI Cliff Cave', world=world))

    # Crater Island abbr. CI
    ciSub2stair = add(Location(name='CI Sub.2 - Stairwell', world=world))
    ciSub2room = add(Location(name='CI Sub.2 - Room', world=world))
    ciSub1stair = add(Location(name='CI Sub.1 - Stairwell', world=world))
    ciSub1room = add(Location(name='CI Sub.1 - Room', world=world))
    ciMainStair = add(Location(name='CI Main Level - Stairwell', world=world))
    ciMainFloor = add(Location(name='CI Main Level', world=world))
    ciObsDeck = add(Location(name='CI Observation Deck', world=world))
    ciTunnel = add(Location(name='CI Crater Tunnel', world=world))
    ciCliffPath = add(Location(name='CI Cliff Path', world=world))
    ciLoadingBay = add(Location(name='CI Loading Bay', world=world))
    ciJetty = add(Location(name='CI Jetty', world=world))

    # PATH DESCRIPTIONS

    # FROM Portal
    add(Path(
        start=fromPortal, destination=towerTop,
        description="YOU ARE AT THE TOP OF THE TOWER. IT HAS A LARGE, SQUARE SURFACE AND A BLACK MARBLE TEXTURE. THE WATER LAPS AT THE EDGES. YOU CAN SEE THREE ISLANDS IN THE DISTANCE."
    ))

    add(Path(
        start=fromPortal, destination=spBeach,
        description="YOU ARE ON A FINE, SANDY BEACH, FACING A THICK FOLIAGE OF TROPICAL FOREST. THERE IS A PATH LEADING IN. THE BEACH CURVES AROUND THE FOREST BOTH WAYS."
    ))

    add(Path(
        start=fromPortal, destination=spRockPool,
        description="YOU ARE ON A SANDY BEACH THAT CURVES AROUND A LUSH, TROPICAL FOREST. BETWEEN IS A GROUPING OF THREE ROCKS, RANGING FROM ONE TO TWO METRES TALL AND AS WIDE AS THE SPAN OF YOUR ARMS STRETCHED OUT."
    ))

    add(Path(
        start=fromPortal, destination=spCaveMouth,
        description="YOU ARE AT THE MOUTH OF A DEEP, DARK CAVE AT THE BOTTOM OF A STEEP CLIFF. YOUR ONLY OPTIONS ARE TO GO INTO THE CAVE OR FOLLOW THE SHALE AND PEBBLE BEACH AROUND TO THE LEFT. AN EERIE GUST CARRYING A SUBTLE SOUND COMES FROM THE CAVE."
    ))

    add(Path(
        start=fromPortal, destination=spTikiPool,
        description="YOU ARE UNDER AN ARCHWAY. THE SPACE YOU ARE IN IS ENCAPSULATED BY FOREST. SOMEONE HAS STRUNG UP A STRING OF COLOURFUL LIGHTBULBS. THERE IS A POOL IN THE CENTRE. IT IS OLD AND DIRTY. IT IS THE SHAPE OF A PEANUT SHELL.TO THE LEFT THERE IS A HUT WITH SOME BAR STOOLS OUT THE FRONT AND A BASEMENT DOOR BEHIND. CLOCKWISE FROM THERE IS A TILED WATERFALL, WHICH LOOKS LIKE IT IS FALLING APART, AND THE ENTRANCE TO A CAVE."
    ))

    add(Path(
        start=fromPortal, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU. THERE IS A DRIED UP FOUNTAINS TO THE LEFT AND A WIDE GRAVEL PATH COVERED IN WEEDS. THERE ARE ARE PATHS BACK INTO THE FOREST TO THE RIGHT AND THE LEFT OF THE RUBBLE."
    ))

    add(Path(
        start=fromPortal, destination=pliBoathouseBay,
        description="YOU ARE IN AN ISOLATED, GREY, SHALE BAY SURROUNDED BY A DENSE FOREST ON THE STEEP SIDE OF THE MOUNTAIN. THERE ARE VARYING SHADES AND SHAPES OF SEAWEEDS AND SHELLS THAT HAVE WASHED ASHORE. TO YOUR LEFT IS A WEATHERED, OLD BOATHOUSE. TO YOUR RIGHT, WHERE THE TEE LINE IS LESS DENSE YOU CAN SEE A WAY INTO THE FOREST. THE OCEAN IS BEHIND YOU."
    ))

    add(Path(
        start=fromPortal, destination=pliRestCabinRm1,
        description="YOU ARE IN A ROOM WITH RECTANGULAR, WOODEN TABLE THAT TAKES UP MOST OF THE CENTRE OF THE SPACE. THERE ARE TWENTY CHAIRS SURROUNDING IT. TWO AT EACH END AND EIGHT ON EACH OF THE LONG SIDES. BEHIND THE END TO YOUR RIGHT IS A LARGE FIREPLACE. THERE IS A FRAME ABOVE IT WITH NO PICTURE AND NOT GLASS. AT THE END TO YOUR LEFT THERE IS A SMALL STOVE AND A SHELF. ACROSS, THERE IS A DOOR TO ANOTHER ROOM."
    ))

    add(Path(
        start=fromPortal, destination=pliBarn,
        description="YOU ARE IN AN EMPTY SPACE. THE ROOF HAS CAVED IN. YOU CAN SEE OUT TO THE SKY. TO THE RIGHT IS A LADDER GOING UP TO A MEZZANINE. TO YOUR LEFT IS A SMALL WINDOW. IT’S QUITE HIGH UP."
    ))

    add(Path(
        start=fromPortal, destination=pliHeliPad,
        description="YOU ARE STANDING ON A HELICOPTER LANDING PAD. THERE IS NO HELICOPTER. THERE ARE CRACKS IN THE ASPHALT AND WILD MOUNTAIN FLOWERS AND SHRUBS CRAWLING THROUGH. FROM HERE YOU CAN SEE OUT TO A MOUNTAIN PEAK AND A PASS BETWEEN HERE AND THERE TO THE RIGHT."
    ))

    add(Path(
        start=fromPortal, destination=pliPass,
        description="YOU CAN SEE OUT TO THE OCEAN IN ONE DIRECTION AND INTO A LAKE BETWEEN TWO MOUNTAINS IN THE OTHER. YOU ARE EXPOSED TO THE ELEMENTS. THERE IS A TRAIL OF FOOTPRINTS LEADING TOWARDS THE OCEAN EDGE, AND ALSO TOWARDS ONE OF THE MOUNTAINS."
    ))

    add(Path(
        start=fromPortal, destination=pliRavineCave,
        description="YOU ARE OUTSIDE A CAVE IN A RAVINE WITH THE RIVER RUNNING BEHIND YOU, FACING A LARGE ROCK WITH DEEP SCRATCHES. THERE ARE MORE SCRATCHES AROUND THE MOUTH OF THE CAVE. INSIDE IS SHALLOW BUT DARK AND DAMP. THERE IS A FEELING OF UNEASE HERE. THE BACK WALL OF THE CAVE GLITCHES AND YOU THINK YOU SEE THE OCEAN."
    ))

    add(Path(
        start=fromPortal, destination=ciSub2room,
        description="YOU ARE IN A WARM, EARTHY, DOMED SPACE. IN THE CENTRE IS A LARGE GLOWING SEMI-SPHERE. SMALL, DIM ORANGE LIGHTS ARE SPACED AROUND THE BOTTOM OF THE WALLS. "
    ))

    add(Path(
        start=fromPortal, destination=ciObsDeck,
        description="YOU ARE AT THE MOUTH OF A CRATER, ON A SEMI-CIRCULAR OBSERVATION DECK LOOKING OUT TO THE OCEAN. THERE IS AN ORNATE BRASS TELESCOPE AND PARK BENCH. THE AREA IS CONTAINED BY A BLACK IRON BARRIER. DOWN BELOW YOU SEE A DENSE FOG THAT SURROUNDS THE ISLAND."
    ))

    add(Path(
        start=fromPortal, destination=ciJetty,
        description="YOU ARE STANDING ON A WEATHERED, CREAKY WOODEN JETTY. THE FOG IS DENSE, YOU CANNOT SEE WHERE IT LEADS."
    ))

    # TO Ocean Surface
    add(Path(
        start=towerTop, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=oceanFloor, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=siSurface, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=spBeach, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=spRockPool, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=spCaveMouth, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=spHarbour, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=pliLanding, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=pliBoathouseBay, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=pliIsolatedBeach, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=ciLoadingBay, destination=oceanSurface,
        description=""
    ))

    add(Path(
        start=ciJetty, destination=oceanSurface,
        description=""
    ))

    # ALL OTHER PATH DESCRIPTIONS BASED ON START LOCATION (rows in matrix)

    # Tower
    add(Path(
        start=oceanSurface, destination=towerTop,
        description="YOU ARE AT THE TOP OF THE TOWER. THE SURFACE IS A LARGE SQUARE AND THE STRUCTURE HAS A BLACK MARBLE TEXTURE. THE WATER LAPS AT THE EDGES. YOU CAN SEE THE ISLANDS IN THE DISTANCE AND A STAIRWAY LEADING DOWN, AROUND THE STRUCTURE TO THE OCEANS DEPTHS."
    ))

    add(Path(
        start=towerTop, destination=towerStairway,
        description="YOU FOLLOW THE STAIRWAY DOWN, AROUND THE TOWER. YOU CAN SEE THE PORTAL ON THE OCEAN BED."
    ))

    add(Path(
        start=towerStairway, destination=towerTop,
        description="YOU ARE AT THE TOP OF THE TOWER. IT HAS A LARGE, SQUARE SURFACE AND A BLACK MARBLE TEXTURE. THE WATER LAPS AT THE EDGES. YOU CAN SEE THREE ISLANDS IN THE DISTANCE."
    ))

    add(Path(
        start=towerStairway, destination=towerBase,
        description="AT THE BASE OF THE TOWER, THE WATER COMES UP TO YOUR ANKLES. YOU CAN SEE THE PORTAL MORE CLEARLY. "
    ))

    add(Path(
        start=towerBase, destination=towerStairway,
        description="AT THE BOTTOM OF THE TOWER IS A STAIRWAY THAT LEADS UP AND AROUND THE TOWER TO THE OCEAN’S MEMBRANE."
    ))

    # Ocean
    add(Path(
        start=oceanSurface, destination=oceanFloor,
        description=""
    ))

    add(Path(
        start=oceanFloor, destination=oceanPortal,
        description="STANDING BY THE PORTAL, YOU FIND THE STRANGE SOUNDS CLEARER…"
    ))

    add(Path(
        start=oceanPortal, destination=oceanFloor,
        description="THE WATER COMES UP TO YOUR ANKLES. DROPS OF WATER FALL FROM ABOVE YOU AND ECHO OMINOUSLY INTO AND FROM THE ABYSS. THERE ARE STRANGE SOUNDS HERE, CRACKLY AND DRY AND GLITCHY…  "
    ))

    # Secret Island
    add(Path(
        start=oceanSurface, destination=siSurface,
        description="YOU ARE ON A SMALL FLOATING ISLAND. IT'S HIGHEST POINT IS ABOUT 6 METRES ABOVE SEA LEVEL. THERE IS A SCRAGGY, THORNY BUSH UP ON TOP. IT SURROUNDS A SMALL SPHERICAL, POLISHED BOULDER."
    ))

    add(Path(
        start=siSurface, destination=siSafeHouse,
        description="YOU ARE IN A WARM SPACE, ENCIRCLED BY A DOME OF SERVERS WITH BLEEPY BLUE AND GREEN LIGHTS. THROUGH THE GLASS BOTTOMED FLOOR YOU CAN SEE THE BED OF THE OCEAN."
    ))

    add(Path(
        start=siSafeHouse, destination=siSurface,
        description="YOU ARE ON A SMALL FLOATING ISLAND. IT'S HIGHEST POINT IS ABOUT 6 METRES ABOVE SEA LEVEL. THERE IS A SCRAGGY, THORNY BUSH UP ON TOP. IT SURROUNDS A SMALL SPHERICAL, POLISHED BOULDER."
    ))

    # Sunshine Plaza
    add(Path(
        start=oceanSurface, destination=spBeach,
        description="YOU ARE ON A FINE, SANDY BEACH, FACING A THICK FOLIAGE OF TROPICAL FOREST. THERE IS A PATH LEADING IN. THE BEACH CURVES AROUND THE FOREST BOTH WAYS."
    ))

    add(Path(
        start=oceanSurface, destination=spRockPool,
        description="YOU ARE ON A SANDY BEACH THAT CURVES AROUND A LUSH, TROPICAL FOREST. BETWEEN IS A GROUPING OF THREE ROCKS, RANGING FROM ONE TO TWO METRES TALL AND AS WIDE AS THE SPAN OF YOUR ARMS STRETCHED OUT."
    ))

    add(Path(
        start=oceanSurface, destination=spCaveMouth,
        description="YOU ARE AT THE MOUTH OF A DEEP, DARK CAVE AT THE BOTTOM OF A STEEP CLIFF. YOUR ONLY OPTIONS ARE TO GO INTO THE CAVE OR FOLLOW THE SHALE AND PEBBLE BEACH AROUND TO THE LEFT. AN EERIE GUST CARRYING A SUBTLE SOUND COMES FROM THE CAVE."
    ))

    add(Path(
        start=oceanSurface, destination=spHarbour,
        description="YOU ALIGHT ONTO A CONCRETE MARINA IN THE SMALL BAY. STANDING TALL BEFORE YOU IS A VERY TALL CANDY STRIPE POLE WITH A CIRCULAR SIGN AT THE TOP, WHICH READS “SUNSHINE PLAZA”. IT GLITCHES AND CHANGES TO “SUNRISE”, “SUNSET’. AT ITS BASE THERE IS THE BUSH OF A DARLINGTONIA CALIFORNICA. BEYOND THE POLE THERE IS A PATH INTO THE FOREST, AND AROUND THE BAY THERE IS ACCESS TO A ROCKY BEACH."
    ))

    add(Path(
        start=spBeach, destination=spBeachToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES."
    ))

    add(Path(
        start=spBeach, destination=spRockPool,
        description="FURTHER ALONG THE BEACH YOU FIND A ROCK POOL. IT IS PART WAY BETWEEN THE OCEAN AND THE FOREST EDGE. THE GROUPING OF THREE ROCKS AROUND THE POOL RANGE FROM ONE TO TWO METRES TALL AND AS WIDE AS THE SPAN OF YOUR ARMS STRETCHED OUT. A SMALL STREAM OF WATER MEANDERS GENTLY BACK TO THE OCEAN."
    ))

    add(Path(
        start=spBeach, destination=spForest,
        description=""
    ))

    add(Path(
        start=spBeach, destination=spCaveMouth,
        description="THE FINE SAND TURNS TO SHALE AND PEBBLES AND THE FOREST IS EVENTUALLY REPLACED BY A STEEP CLIFF. YOU COME TO THE MOUTH OF A DEEP, DARK CAVE AT THE BOTTOM OF THE CLIFF AND FIND YOU CAN’T FOLLOW THE ISLAND AROUND ANY LONGER. AN EERIE GUST CARRYING A SUBTLE SOUND COMES FROM THE CAVE."
    ))

    add(Path(
        start=spBeachToClearing, destination=spBeach,
        description="YOU COME OUT OF THE FOREST ONTO A FINE, SANDY BEACH, WHICH CURVES AROUND THE OUTSIDE OF THE FOREST BOTH WAY. OUT IN FRONT OF YOU, YOU CAN SEE THE OCEAN."
    ))

    add(Path(
        start=spBeachToClearing, destination=spForest,
        description=""
    ))

    add(Path(
        start=spBeachToClearing, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU. THERE ARE TWO DRIED UP FOUNTAINS IN FRONT AND A WIDE GRAVEL PATH COVERED IN WEEDS. THERE ARE ARE PATHS BACK INTO THE FOREST TO THE RIGHT AND THE LEFT OF THE RUBBLE."
    ))

    add(Path(
        start=spRockPool, destination=spBeach,
        description="YOU WALK AROUND WITH THE FOREST ON YOUR LEFT AND THE OCEAN ON YOUR RIGHT, AND YOU CAN SEE THAT IT CONTINUES. YOU FIND A PATH LEADING INTO THE FOREST."
    ))

    add(Path(
        start=spRockPool, destination=spForest,
        description=""
    ))

    add(Path(
        start=spRockPool, destination=spHarbour,
        description="THE SANDY BEACH BECOMES ROCKY AND JAGGED. YOU FOLLOW THE EDGE OF THE FOREST AROUND TO A SMALL MARINA. STANDING TALL BEFORE YOU IS A VERY TALL CANDY STRIPE POLE WITH A CIRCULAR SIGN AT THE TOP, WHICH READS “SUNSHINE PLAZA”. IT GLITCHES AND CHANGES TO “SUNRISE”, “SUNSET’. AT ITS BASE THERE IS THE BUSH OF A DARLINGTONIA CALIFORNICA. THERE IS A PATH TO THE FOREST TO YOUR RIGHT AND THE DOCK ON THE OTHER SIDE OF THE BAY. "
    ))

    add(Path(
        start=spForest, destination=spBeach,
        description="YOU STUMBLE OUT OF THE THICK FOLIAGE ONTO A FINE, SANDY BEACH, WHICH CURVES AROUND THE OUTSIDE OF THE FOREST BOTH WAYS. OUT IN FRONT OF YOU, YOU CAN SEE THE OCEAN. LOOKING BACK TOWARDS THE FOREST, YOU CAN SEE THAT THERE IS A CLEAR PATH LEADING BACK IN."
    ))

    add(Path(
        start=spForest, destination=spBeachToClearing,
        description="YOU STUMBLE ONTO A PATH THAT IS SLIGHTLY OVERGROWN. THE FOLIAGE IS LESS THICK AND YOU CAN SEE UP TO THE CANOPIES."
    ))

    add(Path(
        start=spForest, destination=spRockPool,
        description="YOU STUMBLE OUT OF THE THICK FOLIAGE ONTO A FINE, SANDY BEACH, WHICH CURVES AROUND THE OUTSIDE OF THE FOREST BOTH WAYS. OUT IN FRONT OF YOU, YOU CAN SEE GROUPING OF THREE ROCKS AROUND A SHALLOW POOL THAT RANGE FROM ONE TO TWO METRES TALL AND AS WIDE AS THE SPAN OF YOUR ARMS STRETCHED OUT. BEYOND THAT IS THE OCEAN. "
    ))

    add(Path(
        start=spForest, destination=spTikiPoolToClearing,
        description="YOU STUMBLE ONTO A PATH THAT IS SLIGHTLY OVERGROWN. THE FOLIAGE IS LESS THICK AND YOU CAN SEE UP TO THE CANOPIES."
    ))

    add(Path(
        start=spForest, destination=spHarbourToClearing,
        description="YOU STUMBLE ONTO A PATH THAT IS SLIGHTLY OVERGROWN. THE FOLIAGE IS LESS THICK AND YOU CAN SEE UP TO THE CANOPIES."
    ))

    add(Path(
        start=spForest, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU AND FOUR PATHS EVENLY SPACED."
    ))

    add(Path(
        start=spCaveMouth, destination=spBeach,
        description="YOU WALK AROUND WITH THE ROCKY WALK BECOMING A FOREST ON YOUR RIGHT, AND THE PEBBLES AND SHALE BECOME A FINE, SANDY BEACH. YOU CAN SEE THAT IT CONTINUES AROUND THE FOREST. THE OCEAN IS TO YOUR LEFT. WHERE THE BEACH IS THE CLEAREST, YOU FIND A PATH LEADING INTO THE FOREST."
    ))

    add(Path(
        start=spCaveMouth, destination=spCave,
        description="YOU TAKE A FEW STEPS IN AND FEEL LIGHTER, WEIGHTLESS. YOU FEEL LIKE YOU ARE FLOATING TO THE CAVE’S BREATH’S SONG, THE WATER DRIPPING AROUND YOU BECOMES RHYTHMIC AND MELODIC."
    ))

    add(Path(
        start=spCave, destination=spCaveMouth,
        description="YOU COME OUT OF THE OTHER SIDE OF THE CAVE TO AN EDGE OF THE ISLAND. THE OCEAN IS BREAKING ON THE ROCKS AROUND YOU AND COMES INTO THE CAVE EVER SO SLIGHTLY. ABOVE YOU AND TO YOUR LEFT THERE IS A STEEP CLIFF FACE. IT SEEMS TO SHORTEN, AND THERE IS SPACE TO CONTINUE TO THE RIGHT. "
    ))

    add(Path(
        start=spCave, destination=spTikiPool,
        description="YOU ARE SITTING POOLSIDE. YOU ARE NO ENTIRELY SURE WHEN YOU ARRIVED. THE CAVE IS BEHIND YOU AND THE SPACE YOU ARE IN IS ENCAPSULATED BY FOREST. SOMEONE HAS STRUNG UP A STRING OF COLOURFUL LIGHTBULBS. THE POOL IS OLD AND DIRTY. IT IS THE SHAPE OF A PEANUT SHELL.TO THE LEFT IS AN ARCHWAY MARKING A PATH INTO THE FOREST. CLOCKWISE FROM THERE IS A HUT WITH SOME BAR STOOLS, AND A TILED WATERFALL, WHICH LOOKS LIKE IT IS FALLING APART."
    ))

    add(Path(
        start=spTikiPool, destination=spCave,
        description="THE DAMP, DANK CAVE DRIPS AND GETS NARROWER AND DARKER. THERE IS WATER UP TO YOUR KNEES."
    ))

    add(Path(
        start=spTikiPool, destination=spTikiBar,
        description="YOU ENTER THROUGH THE STRING BEAD DOORWAY, INTO THE BAR. THERE IS A SWITCH TO YOUR RIGHT AND PIN BOARD. ON THE BACK WALL IS A LEDGE AND A COUPLE OF SHELVES WITH EMPTY BOTTLES. AT THE BAR THERE IS A BUILT IN CASH MACHINE, AND UNDERNEATH IS A CRATE. YOU CAN SEE BACK OUT TO THE POOL."
    ))

    add(Path(
        start=spTikiPool, destination=spTikiBasement,
        description="YOU WALK DOWN THE STAIRS TO THE BASEMENT. IT HAS LOW CEILINGS AND YOU HAVE TO CROUCH A BIT. IT IS A SQUARE SPACE WITH A TALL, EMPTY SELF TO THE RIGHT. THERE SOMETHING SCRATCHED INTO THE FAR WALL. THE FLOOR IS COVERED IN BROKEN GLASS AND THERE ARE SOME BULLET HOLES IN THE CEILING."
    ))

    add(Path(
        start=spTikiPool, destination=spTikiPoolToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES. "
    ))

    add(Path(
        start=spTikiBar, destination=spTikiPool,
        description="YOU ARE BACK IN THE POOL AREA. TO YOUR RIGHT THERE IS THE WATERFALL, THEN CLOCKWISE: THE CAVE, AND THE ARCHWAY."
    ))

    add(Path(
        start=spTikiBar, destination=spTikiBasement,
        description="YOU WALK DOWN THE STAIRS TO THE BASEMENT. IT HAS LOW CEILINGS AND YOU HAVE TO CROUCH A BIT. IT IS A SQUARE SPACE WITH A TALL, EMPTY SELF TO THE RIGHT. THERE SOMETHING SCRATCHED INTO THE FAR WALL. THE FLOOR IS COVERED IN BROKEN GLASS AND THERE ARE SOME BULLET HOLES IN THE CEILING."
    ))

    add(Path(
        start=spTikiBasement, destination=spTikiPool,
        description="YOU ARE BACK IN THE POOL AREA. TO YOUR RIGHT THERE IS THE WATERFALL, THEN CLOCKWISE: THE CAVE, AND THE ARCHWAY."
    ))

    add(Path(
        start=spTikiBasement, destination=spTikiBar,
        description="YOU ENTER THROUGH THE STRING BEAD DOORWAY, INTO THE BAR. THERE IS A SWITCH TO YOUR RIGHT AND APIN BOARD. ON THE BACK WALL IS A LEDGE AND A COUPLE OF SHELVES WITH EMPTY BOTTLES. AT THE BAR THERE IS A BUILT IN CASH MACHINE, AND UNDERNEATH IS A CRATE. YOU CAN SEE OUT TO THE POOL.."
    ))

    add(Path(
        start=spTikiPoolToClearing, destination=spForest,
        description=""
    ))

    add(Path(
        start=spTikiPoolToClearing, destination=spTikiPool,
        description="YOU ARE UNDER AN ARCHWAY. THE SPACE YOU ARE IN IS ENCAPSULATED BY FOREST. SOMEONE HAS STRUNG UP A STRING OF COLOURFUL LIGHTBULBS. THERE IS A POOL IN THE CENTRE. IT IS OLD AND DIRTY. IT IS THE SHAPE OF A PEANUT SHELL.TO THE LEFT THERE IS A HUT WITH SOME BAR STOOLS OUT THE FRONT AND A BASEMENT DOOR BEHIND. CLOCKWISE FROM THERE IS A TILED WATERFALL, WHICH LOOKS LIKE IT IS FALLING APART, AND THE ENTRANCE TO A CAVE."
    ))

    add(Path(
        start=spTikiPoolToClearing, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU. THERE IS A DRIED UP FOUNTAINS TO THE LEFT AND A WIDE GRAVEL PATH COVERED IN WEEDS. THERE ARE ARE PATHS BACK INTO THE FOREST TO THE RIGHT AND THE LEFT OF THE RUBBLE."
    ))

    add(Path(
        start=spHarbour, destination=spRockPool,
        description="THE SHALE AND ROCK BECOME A FINE SANDY BEACH WHERE YOU FIND A ROCK POOL. IT IS PART WAY BETWEEN THE OCEAN AND THE FOREST EDGE. THE GROUPING OF THREE ROCKS AROUND THE POOL RANGE FROM ONE TO TWO METRES TALL AND AS WIDE AS THE SPAN OF YOUR ARMS STRETCHED OUT. A SMALL STREAM OF WATER MEANDERS GENTLY BACK TO THE OCEAN."
    ))

    add(Path(
        start=spHarbour, destination=spForest,
        description=""
    ))

    add(Path(
        start=spHarbour, destination=spHarbourToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES. "
    ))

    add(Path(
        start=spHarbourToClearing, destination=spForest,
        description=""
    ))

    add(Path(
        start=spHarbourToClearing, destination=spHarbour,
        description="STANDING TALL BEFORE YOU IS A VERY TALL CANDY STRIPE POLE WITH A CIRCULAR SIGN AT THE TOP, WHICH READS “SUNSHINE PLAZA”. IT GLITCHES AND CHANGES TO “SUNRISE”, “SUNSET’. AT ITS BASE THERE IS THE BUSH OF A DARLINGTONIA CALIFORNICA. BEHIND THIS YOU SEE THE MARINA WITH THE DOCK TO THE RIGHT AND ACCESS TO A ROCKY BEACH TO YOUR LEFT."
    ))

    add(Path(
        start=spHarbourToClearing, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU. THERE ARE ARE PATHS BACK INTO THE FOREST TO THE RIGHT AND THE LEFT OF THE RUBBLE."
    ))

    add(Path(
        start=spMaze, destination=spClearing,
        description="YOU STUMBLE INTO A CLEARING. THERE IS A LARGE PILE OF RUBBLE IN FRONT OF YOU. THERE IS A DRIED UP FOUNTAINS TO THE RIGHT AND A WIDE GRAVEL PATH COVERED IN WEEDS. THERE ARE ARE PATHS BACK INTO THE FOREST TO THE RIGHT AND THE LEFT OF THE RUBBLE."
    ))

    add(Path(
        start=spClearing, destination=spBeachToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES."
    ))

    add(Path(
        start=spClearing, destination=spForest,
        description=""
    ))

    add(Path(
        start=spClearing, destination=spTikiPoolToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES. "
    ))

    add(Path(
        start=spClearing, destination=spHarbourToClearing,
        description="THE PATH IS SLIGHTLY OVERGROWN. THE FOLIAGE IS THICK BUT YOU CAN STILL SEE UP TO THE CANOPIES. "
    ))

    add(Path(
        start=spClearing, destination=spMaze,
        description="YOU FIND YOURSELF AT THE ENTRANCE TO A MAZE. THE PATHS ARE NARROW AS IT HAS NOT BEEN BE MAINTAINED AND THE HEDGES ARE TALL."
    ))

    # Pink Lake Island
    add(Path(
        start=oceanSurface, destination=pliLanding,
        description="YOU ARE ON A PEBBLY BEACH AT THE FOOT OF A TALL MOUNTAIN. IT IS ISOLATED BY THE TREE LINE OF THE FOREST, BUT THERE IS A PATH LEADING IN."
    ))

    add(Path(
        start=oceanSurface, destination=pliBoathouseBay,
        description="YOU ARRIVE AT AN ISOLATED, GREY, SHALE BAY SURROUNDED BY A DENSE FOREST ON THE STEEP SIDE OF THE MOUNTAIN. THERE ARE VARYING SHADES AND SHAPES OF SEAWEEDS AND SHELLS THAT HAVE WASHED ASHORE. TO YOUR LEFT IS A WEATHERED, OLD BOATHOUSE. TO YOUR RIGHT, WHERE THE TEE LINE IS LESS DENSE YOU CAN SEE A WAY INTO THE FOREST."
    ))

    add(Path(
        start=oceanSurface, destination=pliIsolatedBeach,
        description="YOU ALIGHT ONTO A BEACH COVERED IN SHELLS AND SEAWEED,  WHICH POINTS INWARDS TO THE TREE LINE OF A DENSE FOREST. IT LOOKS LIKE YOU CAN FOLLOW THE TOP OF THE POINT IN."
    ))

    add(Path(
        start=pliLanding, destination=pliSkiLiftClearing,
        description="YOU FOLLOW THE PATH THROUGH THE TREES AND TO A CLEARING WHERE YOU FIND THE BOTTOM OF A SKI LIFT AND A SMALL HUT."
    ))

    add(Path(
        start=pliBoathouseBay, destination=pliBoathouse,
        description="THE INSIDE OF THE BOATHOUSE IS COVERED IN COBWEBS. IT CREAKS AND GROANS IN THE WIND."
    ))

    add(Path(
        start=pliBoathouseBay, destination=pliRavineToBrooke_Left,
        description="YOU WALK INTO THE FOREST, FOLLOWING SMALL STREAMS OF WATER THAT HAVE SPLIT FROM A BROOKE YOU FIND FURTHER UP. THE FOREST IS QUIET SAVE FOR SOME CREAKS AND GROANS AND COVERED IN FERNS."
    ))

    add(Path(
        start=pliBoathouse, destination=pliBoathouseBay,
        description="YOU ARE BACK OUT IN THE BAY WHERE YOU CAN FEEL THE SALTY AIR FROM THE OCEAN. IF YOU HEAD STRAIGHT YOU CAN ENTER THE FOREST."
    ))

    add(Path(
        start=pliIsolatedBeach, destination=pliRavineToBrooke_right,
        description="YOU WALK INTO THE FOREST, FOLLOWING SMALL STREAMS OF WATER THAT HAVE SPLIT FROM A BROOKE YOU FIND FURTHER UP. THE FOREST IS QUIET SAVE FOR SOME CREAKS AND GROANS AND COVERED IN FERNS."
    ))

    add(Path(
        start=pliRavine, destination=pliRavineCave,
        description="OUTSIDE THE CAVE IS A LARGE ROCK WITH DEEP SCRATCHES. THERE ARE MORE AROUND THE MOUTH OF THE CAVE. INSIDE IS SHALLOW BUT DARK AND DAMP. THERE IS A FEELING OF UNEASE HERE. THE BACK WALL OF THE CAVE GLITCHES AND YOU THINK YOU SEE THE OCEAN."
    ))

    add(Path(
        start=pliRavine, destination=pliRavineToBrooke_right,
        description="YOU TAKE A RIGHT AT THE FORK AND FOLLOW THE RIVER AS THE WALLS BECOME A FOREST AND THE STREAM BECOMES A BABBLING BROOKE. THE GROUND IS COVERED IN SOFT, BOUNCY BARK PATHS AROUND CROPS OF FERNS."
    ))

    add(Path(
        start=pliRavine, destination=pliRavineToBrooke_Left,
        description="YOU TAKE A RIGHT AT THE FORK AND FOLLOW THE RIVER AS THE WALLS BECOME A FOREST AND THE STREAM BECOMES A BABBLING BROOKE. THE GROUND IS COVERED IN SOFT, BOUNCY BARK PATHS AROUND CROPS OF FERNS."
    ))

    add(Path(
        start=pliRavine, destination=pliNorthShore,
        description="YOU COME TO THE FOOT OF THE MOUNTAIN. THERE IS NO WAY TO CLIMB FROM HERE. THE SMALL BEACH IS ROUGH AND GREY. IN THE LAKE YOU SEE THE REFLECTION OF THE MOUNTAIN ON THE OTHER SIDE OF THE LAKE. YOU SEE THE CHALKY, PINK PARTICLES, YOU SEE… "
    ))

    add(Path(
        start=pliRavine, destination=pliSouthShore,
        description="YOU WALK AUP THIS SIDE OF THE LAKE AND SEE THE TWO CABINS. THE CLOSER ONE IS PART SUBMERGED IN THE LAKE, THE ONE BEHIND IS ON A RISE. BEHIND THIS YOU CAN SEE A PATH LEADING UP THE MOUNTAIN."
    ))

    add(Path(
        start=pliRavineCave, destination=pliRavine,
        description="YOU ARE BACK BY THE RIVER. YOU CAN GO UP OR DOWN STREAM."
    ))

    add(Path(
        start=pliRavineToBrooke_right, destination=pliIsolatedBeach,
        description="YOU FOLLOW THE BROOKE UNTIL IT BREAKS INTO SMALLER, SHALLOWER STREAMS, OUT TO A BEACH COVERED IN SHELLS AND SEAWEED."
    ))

    add(Path(
        start=pliRavineToBrooke_right, destination=pliRavine,
        description="THE BROOKE BECOMES A RIVER AND STEEP WALLS FORM AROUND IT. YOU COME TO A FORK AND CAN CONTINUE UPSTREAM OR TAKE A TURN AROUND THE CORNER ON YOUR LEFT TO FOLLOW IT DOWN A DIFFERENT WAY."
    ))

    add(Path(
        start=pliRavineToBrooke_right, destination=pliLostForest,
        description="YOU HAVE WALKED DEEP INTO THE FOREST AND ARE NOT ENTIRELY SURE WHERE YOU ARE. "
    ))

    add(Path(
        start=pliRavineToBrooke_Left, destination=pliBoathouseBay,
        description="YOU FOLLOW THE BROOKE UNTIL IT BREAKS INTO SMALLER, SHALLOWER STREAMS, OUT TO AN ISOLATED, GREY, SHALE BAY. THERE ARE VARYING SHADES AND SHAPES OF SEAWEEDS AND SHELLS THAT HAVE WASHED ASHORE. TO YOUR RIGHT IS A WEATHERED, OLD BOATHOUSE. AHEAD IS THE OCEAN."
    ))

    add(Path(
        start=pliRavineToBrooke_Left, destination=pliRavine,
        description="THE BROOKE BECOMES A RIVER AND STEEP WALLS FORM AROUND IT. YOU COME TO A FORK AND CAN CONTINUE UPSTREAM OR TAKE A TURN AROUND THE CORNER ON YOUR RIGHT TO FOLLOW IT DOWN A DIFFERENT WAY."
    ))

    add(Path(
        start=pliLostForest, destination=pliBoathouseBay,
        description="THE AIR BECOMES SALTY AND YOU FIND AN ISOLATED, GREY, SHALE BAY. THERE ARE VARYING SHADES AND SHAPES OF SEAWEEDS AND SHELLS THAT HAVE WASHED ASHORE. TO YOUR RIGHT IS A WEATHERED, OLD BOATHOUSE. AHEAD IS THE OCEAN. TO YOUR LEFT IS A WAY BACK INTO THE FOREST."
    ))

    add(Path(
        start=pliLostForest, destination=pliIsolatedBeach,
        description="THE AIR BECOMES SALTY AND YOU FIND AN ISOLATED BEACH COVERED IN SHELLS AND SEAWEED. "
    ))

    add(Path(
        start=pliLostForest, destination=pliRavineToBrooke_right,
        description="YOU FIND A BABBLING BROOKE AND CAN FOLLOW IT UP OR DOWN STREAM."
    ))

    add(Path(
        start=pliLostForest, destination=pliOldTree,
        description="YOU EVENT WANDER INTO A SECLUDED AREA CONTAINING A TWISTED, OLD TREE. IT HAS A WIDE TRUNK WITH A HOLLOW. IT’S THE ONLY TREE LIKE IT THAT YOU HAVE SEEN IN THE FOREST. IT’S LEAVES GLOW."
    ))

    add(Path(
        start=pliLostForest, destination=pliFallingLog,
        description="YOU COME TO A SMALL CLEARING IN THE FOREST. THERE'S THE A SOUND OF SOMETHING LARGE BREAKING BRANCHES ABOVE US AND A LOUD THUD IN THE MIDDLE OF THE CLEARING BUT NOTHING IS VISIBLE."
    ))

    add(Path(
        start=pliLostForest, destination=pliMonMtSlope,
        description="YOU FEEL THE GROUND BENEATH YOU GRADUALLY BECOME MORE OF AN INCLINE. YOU CONTINUE UP AND THE TREES BECOME MORE SPARSE. YOU BEGIN TO FEEL MORE MOVEMENT IN THE AIR AND EVENTUALLY YOU CAN SEE OUT PAST THE TREES AND SEE YOU ARE HIGH UP ON A MOUNTAINSIDE."
    ))

    add(Path(
        start=pliOldTree, destination=pliLostForest,
        description="YOU HAVE WALKED DEEP INTO THE FOREST AND ARE NOT ENTIRELY SURE WHERE YOU ARE. "
    ))

    add(Path(
        start=pliOldTree, destination=pliInsideOldTree,
        description="YOU CIRCLE ROUND AND DOWN THE TUNNEL THAT GOES OFF THE HOLLOW. AS YOU GO FURTHER DOWN THE EARTH AROUND YOU FEELS WARMER AND DRYER. YOU CAN HEAR THE FLICKERING AND THE CRACKLE OF A FIRE. YOU COME TO THE END OF THE TUNNEL AND YOU ARE UNDER A DOME. THERE’S A CRACKLING FIRE THAT SITS ON A ROUND, SMOOTH, LARGE STONE IN THE CENTRE. THERE’S NO FUEL AND YOU DON’T KNOW HOW IT’S LIT. THERE’S NO SMOKE EITHER. THE LIGHT HAS A SEQUENCE OF COLOURS. IT GOES FROM EMERALD TO YELLOW TO FUSHIA."
    ))

    add(Path(
        start=pliInsideOldTree, destination=pliOldTree,
        description="YOU ARE BACK OUT IN THE FOREST."
    ))

    add(Path(
        start=pliFallingLog, destination=pliLostForest,
        description="YOU HAVE WALKED DEEP INTO THE FOREST AND ARE NOT ENTIRELY SURE WHERE YOU ARE. "
    ))

    add(Path(
        start=pliMonMtSlope, destination=pliLostForest,
        description="YOU HAVE WALKED DEEP INTO THE FOREST AND ARE NOT ENTIRELY SURE WHERE YOU ARE. "
    ))

    add(Path(
        start=pliMonMtSlope, destination=pliMonMtPeak,
        description="YOU COME TO THE PEAK OF THE MOUNTAIN WHERE YOU FIND A SHRINE WITH AN OLD BELL SUSPENDED OVER A LARGE SMOOTH STONE. ONLY THE STRUCTURE OF ITS SMALL ROOF REMAINS. ON THE OTHER SIDE OF THE SHRINE YOU CAN SEE A GUIDE POST LEADING TOWARDS A PASS CONNECTING TO THE OTHER MOUNTAIN. BELOW, TO YOUR RIGHT, YOU CAN SEE THE PINK LAKE, AND TO YOUR LEFT, THE OCEAN."
    ))

    add(Path(
        start=pliMonMtPeak, destination=pliMonMtSlope,
        description="THERE IS NO SET PATH DOWN THIS SIDE OF THE MOUNTAIN AND SO YOU ZIGZAG DOWN THE CRAGGY ROCKS, AND THROUGH THE SHRUBS AND INTO FOREST, WHICH BECOMES MORE DENSE."
    ))

    add(Path(
        start=pliMonMtPeak, destination=pliPass,
        description="YOU FOLLOW THE SLOPE DOWN TO THE PASS. YOU CAN SEE OUT TO THE OCEAN AND INTO THE LAKE. YOU ARE EXPOSED TO THE ELEMENTS AND IT DOESN’T LOOK LIKE THERE IS A WAY UP THE OTHER MOUNTAIN FROM HERE. THERE IS A TRAIL OF FOOTPRINTS LEADING TOWARDS THE OCEAN EDGE."
    ))

    add(Path(
        start=pliNorthShore, destination=pliRavine,
        description="YOU FOLLOW THE FOOT OF THE MOUNTAIN TO A POINT IN THE LAKE WHERE IT MEETS THE OTHER MOUNTAIN AND FORMS A RAVINE."
    ))

    add(Path(
        start=pliNorthShore, destination=pliSouthShore,
        description="YOU WALK AROUND THE LAKE, OVER THE OUTLET AND TO THE OTHER SIDE. YOU SEE THE TWO CABINS MORE CLOSELY. THE CLOSER ONE IS PART SUBMERGED IN THE LAKE, THE ONE BEHIND IS ON A RISE. BEHIND THIS YOU CAN SEE A PATH LEADING UP THE MOUNTAIN."
    ))

    add(Path(
        start=pliSouthShore, destination=pliRavine,
        description="YOU FOLLOW THE FOOT OF THE MOUNTAIN TO A POINT IN THE LAKE WHERE IT MEETS THE OTHER MOUNTAIN AND FORMS A RAVINE."
    ))

    add(Path(
        start=pliSouthShore, destination=pliNorthShore,
        description="YOU CIRCLE THE LAKE, OVER THE OUTLET TO THE OTHER SIDE. YOU SEE THE REFLECTION OF THE MOUNTAIN ON THE OTHER SIDE OF THE LAKE. YOU SEE THE CHALKY, PINK PARTICLES, YOU SEE… "
    ))

    add(Path(
        start=pliSouthShore, destination=pliLakeCabin,
        description="YOU ENTER THE CABIN AND ARE IMMEDIATELY CONFRONTED BY A SAB IN A HOLE IN THE FLOOR IN FRONT OF YOU. IT’S TOP HALF HAS COLLAPSED ON TOP OF THE FLOOR AND IT IS COVERED IN RUST. BEHIND IT, IN THE MIDDLE OF THE ROOM IS A DOUBLE BED FRAME, AND BEYOND THAT IS A WIDE BROKEN WINDOW AND THE LAKE WATER THAT HAS CREPT IN. IN THE CORNER TO YOUR LEFT IS A SMALL STOVE."
    ))

    add(Path(
        start=pliSouthShore, destination=pliRiseCabin,
        description="YOU ENTER THE CABIN. IN THE MIDDLE OF THE ROOM IS A DOUBLE BED, AND BEYOND THAT IS A WIDE WINDOW WITH A VIEW OF THE LAKE AND THE MOUNTAIN ACROSS THE WAY. IN THE CORNER TO YOUR LEFT IS A SMALL STOVE, AND AT THE BOTTOM OF THE BED IS AN ORNATE WOODEN CHEST. "
    ))

    add(Path(
        start=pliSouthShore, destination=pliSkiMtSlopeN,
        description="YOU TAKE THE PATH THROUGH THE TREES AND UP TO WHERE IT MEANDERS GENTLY UP THE SIDE OF THE MOUNTAIN. THERE ARE BENCHES ALONG THE WAY SO THAT YOU CAN TAKE IN THE VIEW."
    ))

    add(Path(
        start=pliLakeCabin, destination=pliSouthShore,
        description="YOU ARE BACK OUTSIDE, ON THE SIDE OF THE LAKE."
    ))

    add(Path(
        start=pliRiseCabin, destination=pliSouthShore,
        description="YOU ARE BACK OUTSIDE, ON THE SIDE OF THE LAKE."
    ))

    add(Path(
        start=pliSkiMtSlopeN, destination=pliSouthShore,
        description="YOU MEANDER DOWN THE PATH OF THE MOUNTAIN THROUGH THE TREES AND OUT TO THE SIDE OF THE LAKE. THERE IS A CABIN IN FRONT OF YOU ON A RISE AND ONE FURTHER DOWN TO YOUR LEFT, WHICH LOOKS TO BE PART SUBMERGED. IN THE LAKE YOU CAN SEE THE REFLECTION OF THE MOUNTAIN ON THE OTHER SIDE. THERE IS A SMALL BEACH OVER THERE. DOWN THE LAKESIDE PATH TO YOUR LEFT, WHERE THE MOUNTAINS MEET THERE IS AN OUTLET LEADING INTO A RAVINE."
    ))

    add(Path(
        start=pliSkiMtSlopeN, destination=pliSkiMtPeak,
        description="YOU REACH THE TOP OF THE PATH WHERE THERE IS A SMALL RED FLAG ON A SKI POLE AND A SOLAR FOOTLIGHT WEDGED IN THE SNOW. YOU ARE BEHIND A LARGE MOUND AND CAN SEE THE SIDE OF A SMALL CABIN FROM WHERE YOU ARE."
    ))

    add(Path(
        start=pliSkiMtSlopeS, destination=pliSkiMtPeak,
        description="YOU REACH THE TOP OF THE SKI LIFT WHERE THERE IS A SMALL CONTROL SHED. THERE IS A PATH ACROSS THE PEAK TO SOME STAIRS GOING UP A LARGE MOUND. ANOTHER PATH CROSSES THIS ONE. TO THE LEFT IS A BARN-LIKE STRUCTURE, AND ON THE RIGHT IS A SMALL CABIN."
    ))

    add(Path(
        start=pliSkiMtSlopeS, destination=pliSkiLiftClearing,
        description="YOU FOLLOW THE SLOPE UNDER THE SKI LIFT AND DOWN THROUGH SOME TREES TO A CLEARING WERE THE SKI LIFT ENDS. THERE IS ANOTHER HUT HER LIKE THE ONE AT THE TOP OF THE MOUNTAIN. BEYOND THAT IS A PATH THROUGH THE TREES TOWARDS THE SHORE."
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliSkiMtSlopeN,
        description="YOU MEANDER GENTLY DOWN THE SIDE OF THE MOUNTAIN. THERE ARE BENCHES ALONG THE WAY SO THAT YOU CAN TAKE IN THE VIEW."
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliSkiMtSlopeS,
        description=""
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliRestCabinRm1,
        description="YOU ENTER A ROOM WITH RECTANGULAR, WOODEN TABLE THAT TAKES UP MOST OF THE CENTRE OF THE SPACE. THERE ARE TWENTY CHAIRS SURROUNDING IT. TWO AT EACH END AND EIGHT ON EACH OF THE LONG SIDES. BEHIND THE END TO YOUR RIGHT IS A LARGE FIREPLACE. THERE IS A FRAME ABOVE IT WITH NO PICTURE AND NOT GLASS. AT THE END TO YOUR LEFT THERE IS A SMALL STOVE AND A SHELF. ACROSS, THERE IS A DOOR TO ANOTHER ROOM."
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliBarn,
        description="YOU ARE FACED WITH AN EMPTY SPACE. THE ROOF HAS CAVED IN. YOU CAN SEE OUT TO THE SKY. TO THE RIGHT IS A LADDER GOING UP TO A MEZZANINE. TO YOUR LEFT IS A SMALL WINDOW. IT’S QUITE HIGH UP."
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliSkiLiftTop,
        description="IN THE HUT IS A CONTROL PANEL. THE MAIN LEVER HAS BEEN REPLACED WITH A SNAPPED OFF BIT OF A SKI. THERE IS A BUTTON THAT HAS BEEN LABELLED “SKI LIFT LIGHTS”, THE OTHER BUTTON IS NOT LABELLED. THERE IS WINDOW BEHIND THE PANEL AND YOU CAN SEE THE TOP OF THE SKI LIFT AND OUT AND BEYOND TO THE OCEAN."
    ))

    add(Path(
        start=pliSkiMtPeak, destination=pliHeliPad,
        description="YOU CLIMB THE STAIRS AND FIND YOU ARE STANDING ON A HELICOPTER LANDING PAD. THERE IS NOT HELICOPTER. THERE ARE CRACKS IN THE ASPHALT AND WILD MOUNTAIN FLOWERS AND SHRUBS CRAWLING THROUGH. FROM HERE YOU CAN SEE OUT TO THE OTHER MOUNTAIN PEAK AND THE PASS BETWEEN HERE AND THERE TO THE RIGHT."
    ))

    add(Path(
        start=pliRestCabinRm1, destination=pliSkiMtPeak,
        description="YOU ARE BACK OUTSIDE. THE BARN IS AHEAD OF YOU, THE SKI LIFT TO THE LEFT, AND THE STAIRS UP THE MOUND ON THE RIGHT. YOU CAN ALSO SEE A SMALL RED FLAG BEHIND THE MOUND, AND PAST THAT YOU CAN SEE THE PEAK OF THE OTHER MOUNTAIN IN THE DISTANCE."
    ))

    add(Path(
        start=pliRestCabinRm1, destination=pliRestCabinRm2,
        description="THIS ROOM IS SMALLER. IT CONTAINS TWO BUNK BEDS. ONE IS ALONG THE WALL TO YOUR RIGHT AND ONE ALONG THE WALL YOU FACE. THERE IS A SMALL WINDOW ON THE WALL TO YOUR LEFT. IT HAS THICK RED CURTAINS."
    ))

    add(Path(
        start=pliRestCabinRm2, destination=pliRestCabinRm1,
        description="YOU ARE BACK IN THE MAIN ROOM. YOU CAN SEE OUTSIDE THE TWO WINDOWS EITHER SIDE OF THE DOOR."
    ))

    add(Path(
        start=pliBarn, destination=pliSkiMtPeak,
        description="YOU ARE BACK OUTSIDE. THE SMALL CABIN IS ACROSS FROM YOU. THE SKI LIFT IS TO THE RIGHT, AND THE STAIRS UP THE MOUND ARE TO THE LEFT. PAST THAT YOU CAN SEE THE PEAK OF THE OTHER MOUNTAIN IN THE DISTANCE."
    ))

    add(Path(
        start=pliSkiLiftTop, destination=pliSkiMtPeak,
        description="YOU LEAVE THE CONTROLS. THERE IS A PATH ACROSS THE PEAK TO SOME STAIRS GOING UP A LARGE MOUND. ANOTHER PATH CROSSES THIS ONE. TO THE LEFT IS A BARN-LIKE STRUCTURE, AND ON THE RIGHT IS A SMALL CABIN."
    ))

    add(Path(
        start=pliSkiLiftTop, destination=pliSkiLiftBottom,
        description="AT THE BOTTOM OF THE SKI LIFT YOU ARE DROPPED OFF NEXT TO A HUT ALMOST IDENTICAL TO THE ONE YOU CAME FROM. THIS ONE ALSO HAS TWO BUTTONS, BUT THE LEVER IS STILL INTACT."
    ))

    add(Path(
        start=pliHeliPad, destination=pliSkiMtPeak,
        description="YOU MAKE YOUR WAY BACK DOWN THE STAIRS. ACROSS FROM YOU IS THE SKI LIFT, AT THE CROSSING PATH, THERE IS THE BARN TO YOUR RIGHT AND THE SMALL CABIN TO YOUR LEFT."
    ))

    add(Path(
        start=pliSkiLiftClearing, destination=pliLanding,
        description="YOU ARE ON A PEBBLY BEACH AT THE FOOT OF THE MOUNTAIN. IT IS ISOLATED BY THE TREE LINE OF THE FOREST YOU HAVE COME FROM, WAVES ARE LAPPING AT THE SHORE IN FRONT OF YOU."
    ))

    add(Path(
        start=pliSkiLiftClearing, destination=pliSkiMtSlopeS,
        description=""
    ))

    add(Path(
        start=pliSkiLiftClearing, destination=pliSkiLiftBottom,
        description="IN THE HUT IS A CONTROL PANEL FOR THE SKI LIFT. THE WINDOW ABOVE IT LOOKS UP THE MOUNTAIN TO ANOTHER HUT WHERE THE SKI LIFT ENDS AT THE TOP. THE CONTROL PANEL HAS TWO BUTTONS AND A LEVER."
    ))

    add(Path(
        start=pliSkiLiftBottom, destination=pliSkiLiftTop,
        description="YOU MAKE IT TO THE TOP OF THE SKI LIFT. THERE IS ANOTHER HUT WITH ANOTHER CONTROL PANEL. THE MAIN LEVER IN THIS ONE HAS BEEN REPLACED WITH A SNAPPED OFF BIT OF A SKI. THERE IS A BUTTON THAT HAS BEEN LABELLED “SKI LIFT LIGHTS”, THE OTHER BUTTON IS NOT LABELLED. THERE IS WINDOW BEHIND THE PANEL AND YOU CAN SEE THE TOP OF THE SKI LIFT AND OUT AND BEYOND TO THE OCEAN. OUTSIDE OF THE HUT IT THE PEAK OF THE MOUNTAIN."
    ))

    add(Path(
        start=pliSkiLiftBottom, destination=pliSkiLiftClearing,
        description="YOU ARE BACK OUT IN THE CLEARING."
    ))

    add(Path(
        start=pliPass, destination=pliMonMtPeak,
        description="YOU ARE BACK AT THE PEAK OF THE MOUNTAIN WITH THE SHRINE. TO YOUR LEFT, YOU CAN SEE THE PINK LAKE AND THE OTHER MOUNTAIN. TO YOUR RIGHT, YOU CAN SEE THE OCEAN."
    ))

    add(Path(
        start=pliPass, destination=pliCliffCave,
        description=""
    ))

    add(Path(
        start=pliCliffCave, destination=pliPass,
        description="YOU ARE BACK AT THE PASS LOOKING IN TOWARDS THE SHIMMERING PINK LAKE."
    ))

    # Crater Island
    add(Path(
        start=oceanSurface, destination=ciLoadingBay,
        description="THE FOG IS DENSE AND YOU FIND A DAMP, ALMOST VERTICAL, DARK GREY ROCK WALL THAT CURVES AROUND TO THE LEFT AND RIGHT. YOU CAN HEAR THE SEA AND CREAKING WOOD BEHIND YOU."
    ))

    add(Path(
        start=oceanSurface, destination=ciJetty,
        description="YOU ARRIVE AT A WEATHERED, CREAKY WOODEN JETTY. THE FOG IS DENSE, YOU CANNOT SEE WHERE IT LEADS."
    ))

    add(Path(
        start=ciSub2stair, destination=ciSub2room,
        description="YOU ARE IN A WARM, EARTHY, DOMED SPACE. IN THE CENTRE IS A LARGE GLOWING SEMI-SPHERE. SMALL, DIM ORANGE LIGHTS ARE SPACED AROUND THE BOTTOM OF THE WALLS. "
    ))

    add(Path(
        start=ciSub2stair, destination=ciSub1stair,
        description="YOU ARE IN THE STAIRWELL. YOU CAN GO UP OR DOWN THE STAIRS. THERE IS A DOOR."
    ))

    add(Path(
        start=ciSub2room, destination=ciSub2stair,
        description="YOU ARE IN A DIMLY LIT, ROUND STAIRWELL WITH A SPIRAL METAL STAIRCASE GOING UP. "
    ))

    add(Path(
        start=ciSub1stair, destination=ciSub2stair,
        description="YOU ARE AT THE BOTTOM OF THE STAIRWELL WITH A SPIRAL. THERE IS A DOOR. "
    ))

    add(Path(
        start=ciSub1stair, destination=ciSub1room,
        description="THIS SPACE IS CIRCULAR AND THE CEILINGS ARE LOW. IT IS WARM AND THERE IS A RESONANT HUMMING FROM THE THREE CONTROL STATIONS, WHICH EACH FORM THE POINT OF A TRIANGLE IN THE CENTRE OF THE ROOM."
    ))

    add(Path(
        start=ciSub1stair, destination=ciMainStair,
        description="YOU ARE AT THE TOP OF THE STAIRS. THERE IS A DOOR."
    ))

    add(Path(
        start=ciSub1room, destination=ciSub1stair,
        description="YOU ARE IN A DIMLY LIT, ROUND STAIRWELL WITH A SPIRAL METAL STAIRCASE. YOU CAN GO UP OR DOWN."
    ))

    add(Path(
        start=ciMainStair, destination=ciSub1stair,
        description="DOWN ON THE NEXT LEVEL YOU SEE A DOOR. THERE IS ANOTHER LEVEL BELOW."
    ))

    add(Path(
        start=ciMainStair, destination=ciMainFloor,
        description="YOU FIND YOURSELF THE BOTTOM OF THE INSIDE A LARGE CRATER. A STAIRCASE TO YOUR RIGHT SPIRALS THE WALLS UP TOWARDS THE OPENING. IN FRONT OF YOU, IN THE ROUND SPACE, YOU SEE THREE LARGE MECHANIC PODS WITH STEAM SHOOTING FROM THEIR TOPS. STATIONED AT EACH OF THE PODS IS A CONTROL PANEL. HALFWAY UP THE STAIRS IS A EXIT."
    ))

    add(Path(
        start=ciMainFloor, destination=ciMainStair,
        description="YOU ARE IN A DIMLY LIT, ROUND STAIRWELL WITH A SPIRAL METAL STAIRCASE GOING DOWN."
    ))

    add(Path(
        start=ciMainFloor, destination=ciObsDeck,
        description="AT THE TOP OF THE CRATER YOU FIND AN SEMI-CIRCULAR OBSERVATION DECK LOOKING OUT TO THE OCEAN. THERE IS AN ORNATE BRASS TELESCOPE AND PARK BENCH. THE AREA IS CONTAINED BY A BLACK IRON BARRIER. DOWN BELOW YOU SEE A DENSE FOG THAT SURROUNDS THE ISLAND."
    ))

    add(Path(
        start=ciMainFloor, destination=ciTunnel,
        description="THE WALLS OF THE TUNNEL ARE ROUGH AND A WARMER, EARTHIER TONE THAN INSIDE THE CRATER, AND YOU CAN TOUCH THE CEILING. IT MEANDERS IN A NON-SENSICAL WAY, LIT BY A LINE OF SMALL HALOGEN LIGHTS ON THE RIGHT WALL."
    ))

    add(Path(
        start=ciObsDeck, destination=ciMainFloor,
        description="YOU ARE AT THE TOP OF A STAIRWAY INSIDE THE CRATER. IT SPIRALS THE WALLS DOWN TO THE FLOOR, WHERE YOU SEE THREE LARGE MECHANIC PODS. STEAM SHOOTS FROM THEIR TOPS. AT THE BOTTOM OF EACH OF THE PODS IS A CONTROL PANEL. HALFWAY DOWN, AND AT THE BOTTOM OF THE STAIRS IS A DOORWAY."
    ))

    add(Path(
        start=ciTunnel, destination=ciMainFloor,
        description="YOU ARE HALFWAY UP, INSIDE THE CRATER. YOU ARE ON THE STAIRWELL, WHICH SPIRALS THE WALLS UP TO THE TOP AND DOWN TO THE FLOOR. LOOKING UP YOU CAN SEE THE SKY OUT THE TOP OF THE CRATER. BELOW, YOU SEE THREE LARGE MECHANIC PODS. STEAM SHOOTS FROM THEIR TOPS. AT THE BOTTOM OF EACH OF EACH OF THE PODS IS A CONTROL PANEL. AT THE BOTTOM OF THE STAIRS IS A DOORWAY."
    ))

    add(Path(
        start=ciTunnel, destination=ciCliffPath,
        description="A ROPE LADDER LEADS UP OR DOWN THE OUTER WALL OF THE CRATER. THE FOG IS DENSE AND SURROUNDS YOU."
    ))

    add(Path(
        start=ciCliffPath, destination=ciTunnel,
        description="THE WALLS OF THE TUNNEL ARE ROUGH AND A WARMER, EARTHIER TONE THAN OUTSIDE THE CRATER, AND YOU CAN TOUCH THE CEILING. IT MEANDERS IN A NON-SENSICAL WAY, LIT BY A LINE OF SMALL HALOGEN LIGHTS ON THE LEFT WALL."
    ))

    add(Path(
        start=ciCliffPath, destination=ciLoadingBay,
        description="THE FOG BECOMES LESS DENSE AND YOU CAN HEAR THAT THERE IS MORE SPACE FROM THE SEA. THE GROUND HERE IS PAVED. YOU CAN HEAR THE CREAK OF WOOD BEING MOVED BY WATER."
    ))

    add(Path(
        start=ciLoadingBay, destination=ciCliffPath,
        description="THE PATH LEADS ROUND THE WALL. IT IS NARROW AND ON THE OTHER SIDE OF YOU IS THE FOG AND A STEEP DROP INTO THE OCEAN."
    ))

    add(Path(
        start=ciLoadingBay, destination=ciJetty,
        description="YOU WALK TOWARDS THE CREAKY SOUND AND FIND THE BEGINNING OF A WEATHERED, WOODEN JETTY. THE FOG IS DENSE AND YOU CAN’T SEE HOW FAR IT GOES."
    ))

    add(Path(
        start=ciJetty, destination=ciLoadingBay,
        description="THE FOG IS DENSE AND YOU FIND A DAMP, ALMOST VERTICAL, DARK GREY ROCK WALL THAT CURVES AROUND TO THE LEFT AND RIGHT. YOU CAN HEAR THE SEA BEHIND YOU."
    ))

    # LOCATION INFO

    # Transcient zones
    add(LocationInfo(
        location=fromPortal,
        info=""
    ))

    add(LocationInfo(
        location=oceanSurface,
        info="Depends on weather and time of day"
    ))

    # Ocean zone
    add(LocationInfo(
        location=oceanFloor,
        info="Light has dappled effect from water acting as filter - depends on time of day. Strange whale/submarine sounds - depends on time of day or status of session"
    ))

    add(LocationInfo(
        location=oceanPortal,
        info="Strange sounds are leaks from other (real) world. "
    ))

    # Tower zone
    add(LocationInfo(
        location=towerTop,
        info="The cube: pulses colours (emerald-yellow-fushia-white), top closed. Clanky bell sound."
    ))

    add(LocationInfo(
        location=towerStairway,
        info="No current info."
    ))

    add(LocationInfo(
        location=towerBase,
        info="No current info."
    ))

    # Secret Island abbr. SI
    add(LocationInfo(
        location=siSurface,
        info="Different time-feel: within a space where time moves slower and outer sound is not audible. Can see everything outside speed up. Constant climate: no wind/air movement, cool. Scout feels more energised."
    ))

    add(LocationInfo(
        location=siSafeHouse,
        info="Almost infinity mirror effect with lights on glass."
    ))

    # Sunshine plaza (prev. sunrise/sunset) abbr. SP
    add(LocationInfo(
        location=spBeach,
        info="No current info."
    ))

    add(LocationInfo(
        location=spBeachToClearing,
        info="Sometimes can hear bird calls."
    ))

    add(LocationInfo(
        location=spRockPool,
        info="Water is pearlescent near full moon. NPC: Silvery rock pool snake (back up memory system for world, keeps it functioning). Sometimes in hole in middle emitting bubbles. Can communicate with scouts, holds information about the world - can answer up to 3 questions pp. TOs: Dried up freesia by rock pool."
    ))

    add(LocationInfo(
        location=spForest,
        info="Tangled vines and tree roots… difficult to walk through. Sometimes can hear bird calls."
    ))

    add(LocationInfo(
        location=spCaveMouth,
        info="Sound from cave varies from MUZAK to advertisement for the world. TOs: Paper with \"KNIFE\" written on it wedged in rocks."
    ))

    add(LocationInfo(
        location=spCave,
        info="Only hear music when going to Tiki Pool. Going to ocean is fully conscious experience."
    ))

    add(LocationInfo(
        location=spTikiPool,
        info="Waterfall, colourful lights and pool lights are OFF. TOs: Skeleton in pool. Fallen tiles from waterfall."
    ))

    add(LocationInfo(
        location=spTikiBar,
        info="Light switches: TIKI POOL AREA: OFF. BASEMENT: ON. BAR: ON. Bullet holes in floor, can see into basement if light is on. TOs: Scattered beads. 2 x Ron&Cici photos. Empty bottles. Bullet shells. TWO PHOTOS. THE PHOTOS BOTH HAVE THE SAME COUPLE IN THEM. LEATHERY TANS AND SALT BLEACHED HAIR, RUGGED. ONE IS AT THE TIKI BAR, THE OTHER LOOKS LIKE A CABIN. I POOR THE RUM INTO LJP'S CERAMIC CUP. THE CABIN PHOTO: \"C x\". THE BAR PHOTO \"summum-2689\". THERE ARE 5 LARGE PARTS OF THE PORCELAIN FIGURE AND A FEW CHIPPED BITS. ITS A GEORGIAN LADY WITH A BIG SKIRT."
    ))

    add(LocationInfo(
        location=spTikiBasement,
        info="LIGHT IS ON. TO: Shattered glass. Planks of wood."
    ))

    add(LocationInfo(
        location=spTikiPoolToClearing,
        info="Sometimes can hear bird calls."
    ))

    add(LocationInfo(
        location=spHarbour,
        info="Can see sunken boat from marina dock. TOs: moored row boat."
    ))

    add(LocationInfo(
        location=spHarbourToClearing,
        info="Sometimes hear bird calls."
    ))

    add(LocationInfo(
        location=spMaze,
        info="Refer to map."
    ))

    add(LocationInfo(
        location=spClearing,
        info="TO: Glitchy ghost freesia under awning on steps to hotel ruins. Detached phone in rubble with connection to mountain. "
    ))

    # Pink Lake Island abbr. PLI
    add(LocationInfo(
        location=pliLanding,
        info="TOs: Canoe with oar. Row boat. Rock climbing kit."
    ))

    add(LocationInfo(
        location=pliBoathouseBay,
        info="Potential for wind to be very strong here. TOs: Washed up slightly deflated rubber dingy. Paper note from Monument Mt. Peak."
    ))

    add(LocationInfo(
        location=pliBoathouse,
        info="TO: one canoe with oar on shelf."
    ))

    add(LocationInfo(
        location=pliIsolatedBeach,
        info="No current info."
    ))

    add(LocationInfo(
        location=pliRavine,
        info="Like being between streets of skyscrapers. Very little direct light during the day and acts as brisk wind tunnel. River is generally shallow and calm enough to cross and there is enough space either side to walk."
    ))

    add(LocationInfo(
        location=pliRavineCave,
        info="TOs: 2x sleeping bags. Switch blade. Cut rope around the rock."
    ))

    add(LocationInfo(
        location=pliRavineToBrooke_right,
        info="Brooke/forest: moist and mossy, lots of ferns."
    ))

    add(LocationInfo(
        location=pliRavineToBrooke_Left,
        info="Brooke/forest: moist and mossy, lots of ferns."
    ))

    add(LocationInfo(
        location=pliLostForest,
        info="Dense repetition. Actual looped patch of forest. Has to pass through X number of times before finding the Old Tree, then X/2 to find the log"
    ))

    add(LocationInfo(
        location=pliOldTree,
        info="No current info."
    ))

    add(LocationInfo(
        location=pliInsideOldTree,
        info="Drawing in dirt: heart, clover, question mar, isometric cubes. Fire has special quality and can bring drawings to 3D, also can show mighty bird in bright white light. TOs: Pile of animal hides (15). Cauldron with wood shavings. Whittled spears and stakes. Drone with voice of Henry Rollins on top of animal hides (memory wiped)."
    ))

    add(LocationInfo(
        location=pliFallingLog,
        info="Has to pass through this area (X/2)/2 to find Monument Mt. Slope. TOs: Glitchy ghost log on loop, sound only. Actual log next to ghost log tied to tree. Drawing in dirt \"Don't bother, it's a loop forever\""
    ))

    add(LocationInfo(
        location=pliMonMtSlope ,
        info="No current info."
    ))

    add(LocationInfo(
        location=pliMonMtPeak,
        info="View of Ski Mt. Peak. View of lake, shows differently to from Heli-Pad. Bell sounds without being rung, echoes across lake. TOs: Loose tiles from monument roof."
    ))

    add(LocationInfo(
        location=pliNorthShore,
        info="Looking into lake can be dangerous. Often interrupted by MB call from above, or timely bell. "
    ))

    add(LocationInfo(
        location=pliSouthShore,
        info="Stop to admire the view."
    ))

    add(LocationInfo(
        location=pliLakeCabin ,
        info="TOs: Metal bucket bin. Burnt remains of book in stove (Wild Seed by Octavia E Butler)."
    ))

    add(LocationInfo(
        location=pliRiseCabin,
        info="NPC: SAB #PLI-2-11-12 - stuck in hole in floorboard after spinning. TOs: Blanket."
    ))

    add(LocationInfo(
        location=pliSkiMtSlopeN,
        info="Winding path with rail and lights. Stop to admire the view. Trees less sparse towards top. "
    ))

    add(LocationInfo(
        location=pliSkiMtSlopeS,
        info="Ski lift above on/off, creaking and dropping bits of snow. Stop and admire the view before/after the tree line… can see islands in the distance depending on time of day. Hotel on SP can be visible and other LIVE elements during full moon, including the strings, merging of past/present."
    ))

    add(LocationInfo(
        location=pliSkiMtPeak,
        info="Short red flag and solar powered outdoor foot lamp can be seen from rest cabin and heli-pad. Smells like hot chocolate,  marshmallows and firework smoke."
    ))

    add(LocationInfo(
        location=pliRestCabinRm1,
        info="Feels warm but can see breath as if very cold. TOs: Firewood by stove. 2 x old camping mugs. Kettle on stove. Matches on shelf. "
    ))

    add(LocationInfo(
        location=pliRestCabinRm2,
        info="Can see ski pole and lamp from window. TOs: Blankets on 3 beds."
    ))

    add(LocationInfo(
        location=pliBarn,
        info="Crate on mezzanine. TOs: dust sheet, mismatched skis. Ladder under roof rubble. Ski boots x2. Crate lid. Roof caved in from snow but mezzanine still accessible."
    ))

    add(LocationInfo(
        location=pliSkiLiftTop,
        info="SKI LIFT ON: TOs: Broken ski in place of lever (toxic green with faux tribal pattern in black) wedged in control panel lever"
    ))

    add(LocationInfo(
        location=pliHeliPad,
        info="View of monument mountain. Lake looks pretty and glistens. Shadow figure at the monument"
    ))

    add(LocationInfo(
        location=pliSkiLiftClearing,
        info="TOs: Pile of slalom flags. Bottom of run. "
    ))

    add(LocationInfo(
        location=pliSkiLiftBottom,
        info="SKI LIFT ON."
    ))

    add(LocationInfo(
        location=pliPass,
        info="Occasional encounters with SAB #PLI-2-11-13 if not in cliff cave. Soft snow. Rumbles felt when bell sounds. Crunchier snow up towards Monument Mt. Peak."
    ))

    add(LocationInfo(
        location=pliCliffCave,
        info=" SAB #PLI-2-11-13 is based here. Occasionally out between here and Monument Mt. Peak. Has a small fire going sometimes. "
    ))

    # Crater Island abbr. CI
    add(LocationInfo(
        location=ciSub2stair,
        info="TOs: Tug cart jammed against stair."
    ))

    add(LocationInfo(
        location=ciSub2room,
        info="Orb glows and has warmth. When scout watches for long enough the orb starts to draw energy from the crater until it is able to give live insight into AFK-world via a webcam. NPCs: SABs #CI-3-01-02, -03 & -04 standing around orb.. TOs: Ball of unmelted ice by the orb on the stair side. Remains of SAB #CI-3-01-01 (2nd from left at door clockwise). "
    ))

    add(LocationInfo(
        location=ciSub1stair,
        info="No current info."
    ))

    add(LocationInfo(
        location=ciSub1room,
        info="CONTROL PANELS SLI-1 (CI), SLI-2(SP) & SLI-3(PLI give stats for each island and correlate with REACTORs on floor above. NPCs: SABs #CI-3-02-05, -06 & -07 manning control desks. "
    ))

    add(LocationInfo(
        location=ciMainStair,
        info="No current info."
    ))

    add(LocationInfo(
        location=ciMainFloor,
        info="REACTORS R1(CI), R2(SP), R3 (PLI) (refer to instructions). NPCs: SABs #CI-3-03-08 (working on R1&R2), -09 (piling rocks between stair and R1) & -11(standing in centre, responsive). Marks in the ground from previous session now permanent in centre of space \"10 1100 111000…..can u understand me?\" // \“∞>>>>>º-º/_º-º_º-º_º-º_º-º_/∞\”. TOs: Remains of SAB #CI-3–03-10."
    ))

    add(LocationInfo(
        location=ciObsDeck,
        info="Limits of ORB power as power source by proximity. Can sometimes see large cloud slowly spinning in place."
    ))

    add(LocationInfo(
        location=ciTunnel,
        info="No current info."
    ))

    add(LocationInfo(
        location=ciCliffPath,
        info="Rope ladder leading to tunnel. Faded red spray paint on crater at bottom of stairs \“I WAS HERE\”. TOs: Strand of yellow/purple wool caught in ladder."
    ))

    add(LocationInfo(
        location=ciLoadingBay,
        info="No current info."
    ))

    add(LocationInfo(
        location=ciJetty,
        info="Takes until near the end of the jetty to come out of the fog. Can then see the island and out to sea."
    ))

    # ADD SESSION
    add(Session(
        code='TestSession1', active=True,
        current_location=towerTop, previous_location=fromPortal))

    db.session.commit()


if __name__ == '__main__':
    create_test_world()
