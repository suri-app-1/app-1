"""
Central Transformation Configuration
Single source of truth for all transformation parameters in the application

All components should import parameters from this file to ensure consistency.
"""

# =====================================================================
# TRANSFORMATION PARAMETERS - SINGLE SOURCE OF TRUTH
# =====================================================================

# Shear transformation parameters
SHEAR_ANGLE_MIN = -30
SHEAR_ANGLE_MAX = 30
SHEAR_ANGLE_DEFAULT = 0
SHEAR_ANGLE_STEP = 0.1

# Rotation parameters
ROTATION_ANGLE_MIN = -180
ROTATION_ANGLE_MAX = 180
ROTATION_ANGLE_DEFAULT = 0
ROTATION_ANGLE_STEP = 0.1

# Brightness parameters
BRIGHTNESS_MIN = 0.5
BRIGHTNESS_MAX = 1.5
BRIGHTNESS_DEFAULT = 1.0
BRIGHTNESS_STEP = 0.01

# Contrast parameters
CONTRAST_MIN = 0.5
CONTRAST_MAX = 1.5
CONTRAST_DEFAULT = 1.0
CONTRAST_STEP = 0.01

# Blur parameters
BLUR_RADIUS_MIN = 0.5
BLUR_RADIUS_MAX = 20.0
BLUR_RADIUS_DEFAULT = 2.0
BLUR_RADIUS_STEP = 0.1

# Hue parameters
HUE_SHIFT_MIN = -30
HUE_SHIFT_MAX = 30
HUE_SHIFT_DEFAULT = 0
HUE_SHIFT_STEP = 0.1

# Saturation parameters
SATURATION_MIN = 0.5
SATURATION_MAX = 1.5
SATURATION_DEFAULT = 1.0
SATURATION_STEP = 0.01

# Gamma parameters
GAMMA_MIN = 0.5
GAMMA_MAX = 2.0
GAMMA_DEFAULT = 1.0
GAMMA_STEP = 0.01

# Resize parameters
RESIZE_WIDTH_MIN = 64
RESIZE_WIDTH_MAX = 4096
RESIZE_WIDTH_DEFAULT = 640
RESIZE_HEIGHT_MIN = 64
RESIZE_HEIGHT_MAX = 4096
RESIZE_HEIGHT_DEFAULT = 640

# =====================================================================
# TRANSFORMATION CATEGORIES
# =====================================================================

# List of transformations that support negative values (for Smart & Minimal Strategy)
SYMMETRIC_TRANSFORMATIONS = [
    'rotate', 'brightness', 'contrast', 'shear', 'hue', 'saturation', 'gamma'
]

# Transformation categories
BASIC_TRANSFORMATIONS = [
    'resize', 'rotate', 'flip', 'brightness', 'contrast', 'blur'
]

ADVANCED_TRANSFORMATIONS = [
    'shear', 'hue', 'saturation', 'gamma'
]

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def get_shear_parameters():
    """Get shear transformation parameters"""
    return {
        'min': SHEAR_ANGLE_MIN,
        'max': SHEAR_ANGLE_MAX,
        'default': SHEAR_ANGLE_DEFAULT,
        'step': SHEAR_ANGLE_STEP
    }

def get_rotation_parameters():
    """Get rotation transformation parameters"""
    return {
        'min': ROTATION_ANGLE_MIN,
        'max': ROTATION_ANGLE_MAX,
        'default': ROTATION_ANGLE_DEFAULT,
        'step': ROTATION_ANGLE_STEP
    }

def get_brightness_parameters():
    """Get brightness transformation parameters"""
    return {
        'min': BRIGHTNESS_MIN,
        'max': BRIGHTNESS_MAX,
        'default': BRIGHTNESS_DEFAULT,
        'step': BRIGHTNESS_STEP
    }

def get_contrast_parameters():
    """Get contrast transformation parameters"""
    return {
        'min': CONTRAST_MIN,
        'max': CONTRAST_MAX,
        'default': CONTRAST_DEFAULT,
        'step': CONTRAST_STEP
    }

def get_blur_parameters():
    """Get blur transformation parameters"""
    return {
        'min': BLUR_RADIUS_MIN,
        'max': BLUR_RADIUS_MAX,
        'default': BLUR_RADIUS_DEFAULT,
        'step': BLUR_RADIUS_STEP
    }

def get_hue_parameters():
    """Get hue transformation parameters"""
    return {
        'min': HUE_SHIFT_MIN,
        'max': HUE_SHIFT_MAX,
        'default': HUE_SHIFT_DEFAULT,
        'step': HUE_SHIFT_STEP
    }

def get_saturation_parameters():
    """Get saturation transformation parameters"""
    return {
        'min': SATURATION_MIN,
        'max': SATURATION_MAX,
        'default': SATURATION_DEFAULT,
        'step': SATURATION_STEP
    }

def get_gamma_parameters():
    """Get gamma transformation parameters"""
    return {
        'min': GAMMA_MIN,
        'max': GAMMA_MAX,
        'default': GAMMA_DEFAULT,
        'step': GAMMA_STEP
    }

def get_resize_parameters():
    """Get resize transformation parameters"""
    return {
        'width': {
            'min': RESIZE_WIDTH_MIN,
            'max': RESIZE_WIDTH_MAX,
            'default': RESIZE_WIDTH_DEFAULT
        },
        'height': {
            'min': RESIZE_HEIGHT_MIN,
            'max': RESIZE_HEIGHT_MAX,
            'default': RESIZE_HEIGHT_DEFAULT
        }
    }