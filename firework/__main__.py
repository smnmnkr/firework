from firework import Firework

# -- Start Firework
Firework({
    'title': 'Firework',
    'screenSize': [1200, 700],
    'fps': 24,
    'force': [0.0, 0.015],
    'count': 32,
    'rocket': {
        'size': 3,
        'velocity': [[-2, 2], [-18, -8]],
        'splitterNum': 48,
        'splitterSize': 1,
        'splitterVelocity': 3,
        'splitterForce': [0.0, 0.005],
        'splitterBrightness': [128, 255],
    }
})
