[
    {
        "id": "ebf804a1.f54e48",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "b8229601.972978",
        "type": "rpi-gpio in",
        "z": "ebf804a1.f54e48",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 144,
        "y": 323,
        "wires": [
            [
                "808b3af6.b2edb8",
                "2eeca598.b7cc0a"
            ]
        ]
    },
    {
        "id": "808b3af6.b2edb8",
        "type": "debug",
        "z": "ebf804a1.f54e48",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 576,
        "y": 317,
        "wires": []
    },
    {
        "id": "4102b8a4.9023b8",
        "type": "rpi-gpio out",
        "z": "ebf804a1.f54e48",
        "name": "LED",
        "pin": "11",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 690,
        "y": 400,
        "wires": []
    },
    {
        "id": "2eeca598.b7cc0a",
        "type": "switch",
        "z": "ebf804a1.f54e48",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 290,
        "y": 380,
        "wires": [
            [
                "1d7253dc.fac0dc"
            ],
            [
                "8016e5e3.c41898"
            ]
        ]
    },
    {
        "id": "1d7253dc.fac0dc",
        "type": "change",
        "z": "ebf804a1.f54e48",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 490,
        "y": 360,
        "wires": [
            [
                "4102b8a4.9023b8"
            ]
        ]
    },
    {
        "id": "8016e5e3.c41898",
        "type": "change",
        "z": "ebf804a1.f54e48",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 490,
        "y": 420,
        "wires": [
            [
                "4102b8a4.9023b8"
            ]
        ]
    }
]
