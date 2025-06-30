properties = {
    "INPUT": [
    ],
    "DENSE": [
        (
            "Units",
            "int",
            {}
        ),
        (
            "Activation",
            "combobox",
            {"values": ["ReLU", "Sigmoid", "Softmax", "Tanh"], "default": "ReLU"}
        ),
    ],
    "CONV1D": [
        (
            "Filters",
            "int",
            {"default": "32"}
        ),
        (
            "Kernel Size",
            "combobox",
            {"values": ["3", "5", "7", "9"], "default": "32"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        ),
        (
            "Padding",
            "combobox",
            {"values": ["None", "Valid", "Same"], "default": "None"}
        ),
        (
            "Activation",
            "combobox",
            {"values": ["ReLU", "Sigmoid", "Tanh"], "default": "ReLU"}
        ),
    ],
    "CONV2D": [
        (
            "Filters",
            "int",
            {"default": "32"}
        ),
        (
            "Kernel Size",
            "combobox",
            {"values": ["3", "5", "7", "9"], "default": "3"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        ),
        (
            "Padding",
            "combobox",
            {"values": ["None", "Valid", "same"], "default": "None"}
        ),
        (
            "Activation",
            "combobox",
            {"values": ["ReLU", "Sigmoid", "Tanh"], "default": "ReLU"}
        ),
    ],
    "MAXPOOLING1D": [
        (
            "Pool Size",
            "int",
            {"default": "2"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        )
    ],
    "MAXPOOLING2D": [
(
            "Pool Size",
            "int",
            {"default": "2"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        )
    ],
    "AVGPOOLING1D": [
(
            "Pool Size",
            "int",
            {"default": "2"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        )
    ],
    "AVGPOOLING2D": [
        (
            "Pool Size",
            "int",
            {"default": "2"}
        ),
        (
            "Strides",
            "int",
            {"default": "2"}
        )
    ],
    "FLATTEN": [
    #     No Properties for Flatten Layer
    ],
    "DROPOUT": [
        (
            "DropOut Percentage",
            "decimal",
            {"default": "0.3"}
        )
    ],

}