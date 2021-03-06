[
    {
        "id": "ebf804a1.f54e48",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "c9308f4b.1c491",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "c195f985.74dda8",
        "type": "tab",
        "label": "Flow 3"
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
    },
    {
        "id": "f7a07561.2bee18",
        "type": "inject",
        "z": "c9308f4b.1c491",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 205,
        "y": 177,
        "wires": [
            [
                "8b97d0c6.c28ce",
                "9dd6b2cb.dd4b"
            ]
        ]
    },
    {
        "id": "8b97d0c6.c28ce",
        "type": "function",
        "z": "c9308f4b.1c491",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"0H0vY6XbZxrfQAM3\"\n    };\n    \nmsg.payload=\"Temperature,,20.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 251,
        "wires": [
            [
                "12af81f3.900d3e"
            ]
        ]
    },
    {
        "id": "12af81f3.900d3e",
        "type": "http request",
        "z": "c9308f4b.1c491",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DGCRKeyJ/datapoints.csv",
        "tls": "",
        "x": 550,
        "y": 220,
        "wires": [
            [
                "661eb654.019a08",
                "7f1cdcc3.fd4c74"
            ]
        ]
    },
    {
        "id": "661eb654.019a08",
        "type": "http response",
        "z": "c9308f4b.1c491",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 220,
        "wires": []
    },
    {
        "id": "7f1cdcc3.fd4c74",
        "type": "debug",
        "z": "c9308f4b.1c491",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 770,
        "y": 320,
        "wires": []
    },
    {
        "id": "9dd6b2cb.dd4b",
        "type": "function",
        "z": "c9308f4b.1c491",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"0H0vY6XbZxrfQAM3\"\n    };\n    \nmsg.payload=\"Humidity,,50.6\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 320,
        "wires": [
            [
                "2471af80.203ae"
            ]
        ]
    },
    {
        "id": "2471af80.203ae",
        "type": "http request",
        "z": "c9308f4b.1c491",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DGCRKeyJ/datapoints.csv",
        "tls": "",
        "x": 570,
        "y": 320,
        "wires": [
            [
                "661eb654.019a08",
                "7f1cdcc3.fd4c74"
            ]
        ]
    },
    {
        "id": "d6dfa7ae.d1f108",
        "type": "inject",
        "z": "c195f985.74dda8",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 151,
        "y": 109,
        "wires": [
            [
                "f851ff01.20cf9"
            ]
        ]
    },
    {
        "id": "f851ff01.20cf9",
        "type": "function",
        "z": "c195f985.74dda8",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"0H0vY6XbZxrfQAM3\"\n    };\n    msg.payload=\"Temperature,,20.3\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 120,
        "wires": [
            [
                "13fc3608.c1fc8a"
            ]
        ]
    },
    {
        "id": "13fc3608.c1fc8a",
        "type": "http request",
        "z": "c195f985.74dda8",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DGCRKeyJ/datapoints.csv",
        "tls": "",
        "x": 549,
        "y": 125,
        "wires": [
            [
                "dda761a.ac520a",
                "d8cf6eb3.73234"
            ]
        ]
    },
    {
        "id": "dda761a.ac520a",
        "type": "http response",
        "z": "c195f985.74dda8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 127,
        "wires": []
    },
    {
        "id": "d8cf6eb3.73234",
        "type": "debug",
        "z": "c195f985.74dda8",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 740,
        "y": 219,
        "wires": []
    }
]
