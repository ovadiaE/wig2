def particles_json(color):
    return {
    "background": {
        "color": {
            "value": "#282c34"
        }
    },
    "detectRetina": True,
    "fpsLimit": 150,
    "interactivity": {
        "events": {
            "onClick": {
                "enable": False,
                "mode": "push"
            },
            "onHover": {
                "enable": False,
                "mode": "repulse"
            },
            "resize": True
        },
        "modes": {
            "push": {
                "quantity": 4
            },
            "repulse": {
                "distance": 200,
                "duration": 0.4
            }
        }
    },
    "particles": {
        "collisions": {
            "enable": False
        },
        "color": {
            "value": color
        },
        "links": {
            "color": "#ffffff",
            "distance": 150,
            "enable": True,
            "opacity": 0.5,
            "width": 1
        },
        "move": {
            "direction": "up",
            "enable": True,
            "outModes": {
                "default": "bounce"
            },
            "random": False,
            "speed": 6,
            "straight": True
        },
        "number": {
            "density": {
                "enable": True,
                "value_area": 800
            },
            "value": 80
        },
        "opacity": {
            "value": 0.5
        },
        "shape": {
            "type": "circle"
        },
        "size": {
            "random": True,
            "value": 5
        }
    }
}