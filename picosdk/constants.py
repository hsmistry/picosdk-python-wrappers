#
# Copyright (C) 2014-2017 Pico Technology Ltd. See LICENSE file for terms.
#
"""
Defines python-visible versions of preprocessor-macros from Pico SDK C header files.
All constants in this file are exposed directly on the Library class specific to each driver. That
(rather than importing this file directly) is the supported way of accessing them, since some
older drivers have different names/values for some of the macros.
"""


class UnknownConstantError(Exception):
    pass


# convenience functions provided in the old python SDK:
def pico_tag(number):
    """Get the macro name for a given PICO_STATUS value."""
    try:
        return PICO_STATUS_LOOKUP[number]
    except KeyError:
        raise UnknownConstantError("%s is not a known PICO_STATUS value." % number)


def pico_num(tag):
    """Resolve the numerical constant associated with a PICO_STATUS macro."""
    try:
        return PICO_STATUS[tag]
    except KeyError:
        raise UnknownConstantError("%s is not a known PICO_STATUS macro." % tag)


def make_enum(members):
    """All C enums with no specific values follow the pattern 0, 1, 2... in the order they are in source."""
    return {member: i for i, member in enumerate(members)}


PICO_STATUS = {
    "PICO_OK": 0x00000000,
    "PICO_MAX_UNITS_OPENED": 0x00000001,
    "PICO_MEMORY_FAIL": 0x00000002,
    "PICO_NOT_FOUND": 0x00000003,
    "PICO_FW_FAIL": 0x00000004,
    "PICO_OPEN_OPERATION_IN_PROGRESS": 0x00000005,
    "PICO_OPERATION_FAILED": 0x00000006,
    "PICO_NOT_RESPONDING": 0x00000007,
    "PICO_CONFIG_FAIL": 0x00000008,
    "PICO_KERNEL_DRIVER_TOO_OLD": 0x00000009,
    "PICO_EEPROM_CORRUPT": 0x0000000A,
    "PICO_OS_NOT_SUPPORTED": 0x0000000B,
    "PICO_INVALID_HANDLE": 0x0000000C,
    "PICO_INVALID_PARAMETER": 0x0000000D,
    "PICO_INVALID_TIMEBASE": 0x0000000E,
    "PICO_INVALID_VOLTAGE_RANGE": 0x0000000F,
    "PICO_INVALID_CHANNEL": 0x00000010,
    "PICO_INVALID_TRIGGER_CHANNEL": 0x00000011,
    "PICO_INVALID_CONDITION_CHANNEL": 0x00000012,
    "PICO_NO_SIGNAL_GENERATOR": 0x00000013,
    "PICO_STREAMING_FAILED": 0x00000014,
    "PICO_BLOCK_MODE_FAILED": 0x00000015,
    "PICO_NULL_PARAMETER": 0x00000016,
    "PICO_ETS_MODE_SET": 0x00000017,
    "PICO_DATA_NOT_AVAILABLE": 0x00000018,
    "PICO_STRING_BUFFER_TO_SMALL": 0x00000019,
    "PICO_ETS_NOT_SUPPORTED": 0x0000001A,
    "PICO_AUTO_TRIGGER_TIME_TO_SHORT": 0x0000001B,
    "PICO_BUFFER_STALL": 0x0000001C,
    "PICO_TOO_MANY_SAMPLES": 0x0000001D,
    "PICO_TOO_MANY_SEGMENTS": 0x0000001E,
    "PICO_PULSE_WIDTH_QUALIFIER": 0x0000001F,
    "PICO_DELAY": 0x00000020,
    "PICO_SOURCE_DETAILS": 0x00000021,
    "PICO_CONDITIONS": 0x00000022,
    "PICO_USER_CALLBACK": 0x00000023,
    "PICO_DEVICE_SAMPLING": 0x00000024,
    "PICO_NO_SAMPLES_AVAILABLE": 0x00000025,
    "PICO_SEGMENT_OUT_OF_RANGE": 0x00000026,
    "PICO_BUSY": 0x00000027,
    "PICO_STARTINDEX_INVALID": 0x00000028,
    "PICO_INVALID_INFO": 0x00000029,
    "PICO_INFO_UNAVAILABLE": 0x0000002A,
    "PICO_INVALID_SAMPLE_INTERVAL": 0x0000002B,
    "PICO_TRIGGER_ERROR": 0x0000002C,
    "PICO_MEMORY": 0x0000002D,
    "PICO_SIG_GEN_PARAM": 0x0000002E,
    "PICO_SHOTS_SWEEPS_WARNING": 0x0000002F,
    "PICO_SIGGEN_TRIGGER_SOURCE": 0x00000030,
    "PICO_AUX_OUTPUT_CONFLICT": 0x00000031,
    "PICO_AUX_OUTPUT_ETS_CONFLICT": 0x00000032,
    "PICO_WARNING_EXT_THRESHOLD_CONFLICT": 0x00000033,
    "PICO_WARNING_AUX_OUTPUT_CONFLICT": 0x00000034,
    "PICO_SIGGEN_OUTPUT_OVER_VOLTAGE": 0x00000035,
    "PICO_DELAY_NULL": 0x00000036,
    "PICO_INVALID_BUFFER": 0x00000037,
    "PICO_SIGGEN_OFFSET_VOLTAGE": 0x00000038,
    "PICO_SIGGEN_PK_TO_PK": 0x00000039,
    "PICO_CANCELLED": 0x0000003A,
    "PICO_SEGMENT_NOT_USED": 0x0000003B,
    "PICO_INVALID_CALL": 0x0000003C,
    "PICO_GET_VALUES_INTERRUPTED": 0x0000003D,
    "PICO_NOT_USED": 0x0000003F,
    "PICO_INVALID_SAMPLERATIO": 0x00000040,
    "PICO_INVALID_STATE": 0x00000041,
    "PICO_NOT_ENOUGH_SEGMENTS": 0x00000042,
    "PICO_DRIVER_FUNCTION": 0x00000043,
    "PICO_RESERVED": 0x00000044,
    "PICO_INVALID_COUPLING": 0x00000045,
    "PICO_BUFFERS_NOT_SET": 0x00000046,
    "PICO_RATIO_MODE_NOT_SUPPORTED": 0x00000047,
    "PICO_RAPID_NOT_SUPPORT_AGGREGATION": 0x00000048,
    "PICO_INVALID_TRIGGER_PROPERTY": 0x00000049,
    "PICO_INTERFACE_NOT_CONNECTED": 0x0000004A,
    "PICO_RESISTANCE_AND_PROBE_NOT_ALLOWED": 0x0000004B,
    "PICO_POWER_FAILED": 0x0000004C,
    "PICO_SIGGEN_WAVEFORM_SETUP_FAILED": 0x0000004D,
    "PICO_FPGA_FAIL": 0x0000004E,
    "PICO_POWER_MANAGER": 0x0000004F,
    "PICO_INVALID_ANALOGUE_OFFSET": 0x00000050,
    "PICO_PLL_LOCK_FAILED": 0x00000051,
    "PICO_ANALOG_BOARD": 0x00000052,
    "PICO_CONFIG_FAIL_AWG": 0x00000053,
    "PICO_INITIALISE_FPGA": 0x00000054,
    "PICO_EXTERNAL_FREQUENCY_INVALID": 0x00000056,
    "PICO_CLOCK_CHANGE_ERROR": 0x00000057,
    "PICO_TRIGGER_AND_EXTERNAL_CLOCK_CLASH": 0x00000058,
    "PICO_PWQ_AND_EXTERNAL_CLOCK_CLASH": 0x00000059,
    "PICO_UNABLE_TO_OPEN_SCALING_FILE": 0x0000005A,
    "PICO_MEMORY_CLOCK_FREQUENCY": 0x0000005B,
    "PICO_I2C_NOT_RESPONDING": 0x0000005C,
    "PICO_NO_CAPTURES_AVAILABLE": 0x0000005D,
    "PICO_NOT_USED_IN_THIS_CAPTURE_MODE": 0x0000005E,
    "PICO_TOO_MANY_TRIGGER_CHANNELS_IN_USE": 0x0000005F,
    "PICO_INVALID_TRIGGER_DIRECTION": 0x00000060,
    "PICO_INVALID_TRIGGER_STATES": 0x00000061,
    "PICO_GET_DATA_ACTIVE": 0x00000103,
    "PICO_IP_NETWORKED": 0x00000104,
    "PICO_INVALID_IP_ADDRESS": 0x00000105,
    "PICO_IPSOCKET_FAILED": 0x00000106,
    "PICO_IPSOCKET_TIMEDOUT": 0x00000107,
    "PICO_SETTINGS_FAILED": 0x00000108,
    "PICO_NETWORK_FAILED": 0x00000109,
    "PICO_WS2_32_DLL_NOT_LOADED": 0x0000010A,
    "PICO_INVALID_IP_PORT": 0x0000010B,
    "PICO_COUPLING_NOT_SUPPORTED": 0x0000010C,
    "PICO_BANDWIDTH_NOT_SUPPORTED": 0x0000010D,
    "PICO_INVALID_BANDWIDTH": 0x0000010E,
    "PICO_AWG_NOT_SUPPORTED": 0x0000010F,
    "PICO_ETS_NOT_RUNNING": 0x00000110,
    "PICO_SIG_GEN_WHITENOISE_NOT_SUPPORTED": 0x00000111,
    "PICO_SIG_GEN_WAVETYPE_NOT_SUPPORTED": 0x00000112,
    "PICO_INVALID_DIGITAL_PORT": 0x00000113,
    "PICO_INVALID_DIGITAL_CHANNEL": 0x00000114,
    "PICO_INVALID_DIGITAL_TRIGGER_DIRECTION": 0x00000115,
    "PICO_SIG_GEN_PRBS_NOT_SUPPORTED": 0x00000116,
    "PICO_ETS_NOT_AVAILABLE_WITH_LOGIC_CHANNELS": 0x00000117,
    "PICO_WARNING_REPEAT_VALUE": 0x00000118,
    "PICO_POWER_SUPPLY_CONNECTED": 0x00000119,
    "PICO_POWER_SUPPLY_NOT_CONNECTED": 0x0000011A,
    "PICO_POWER_SUPPLY_REQUEST_INVALID": 0x0000011B,
    "PICO_POWER_SUPPLY_UNDERVOLTAGE": 0x0000011C,
    "PICO_CAPTURING_DATA": 0x0000011D,
    "PICO_USB3_0_DEVICE_NON_USB3_0_PORT": 0x0000011E,
    "PICO_NOT_SUPPORTED_BY_THIS_DEVICE": 0x0000011F,
    "PICO_INVALID_DEVICE_RESOLUTION": 0x00000120,
    "PICO_INVALID_NUMBER_CHANNELS_FOR_RESOLUTION": 0x00000121,
    "PICO_CHANNEL_DISABLED_DUE_TO_USB_POWERED": 0x00000122,
    "PICO_SIGGEN_DC_VOLTAGE_NOT_CONFIGURABLE": 0x00000123,
    "PICO_NO_TRIGGER_ENABLED_FOR_TRIGGER_IN_PRE_TRIG": 0x00000124,
    "PICO_TRIGGER_WITHIN_PRE_TRIG_NOT_ARMED": 0x00000125,
    "PICO_TRIGGER_WITHIN_PRE_NOT_ALLOWED_WITH_DELAY": 0x00000126,
    "PICO_TRIGGER_INDEX_UNAVAILABLE": 0x00000127,
    "PICO_AWG_CLOCK_FREQUENCY": 0x00000128,
    "PICO_TOO_MANY_CHANNELS_IN_USE": 0x00000129,
    "PICO_NULL_CONDITIONS": 0x0000012A,
    "PICO_DUPLICATE_CONDITION_SOURCE": 0x0000012B,
    "PICO_INVALID_CONDITION_INFO": 0x0000012C,
    "PICO_SETTINGS_READ_FAILED": 0x0000012D,
    "PICO_SETTINGS_WRITE_FAILED": 0x0000012E,
    "PICO_ARGUMENT_OUT_OF_RANGE": 0x0000012F,
    "PICO_HARDWARE_VERSION_NOT_SUPPORTED": 0x00000130,
    "PICO_DIGITAL_HARDWARE_VERSION_NOT_SUPPORTED": 0x00000131,
    "PICO_ANALOGUE_HARDWARE_VERSION_NOT_SUPPORTED": 0x00000132,
    "PICO_UNABLE_TO_CONVERT_TO_RESISTANCE": 0x00000133,
    "PICO_DUPLICATED_CHANNEL": 0x00000134,
    "PICO_INVALID_RESISTANCE_CONVERSION": 0x00000135,
    "PICO_INVALID_VALUE_IN_MAX_BUFFER": 0x00000136,
    "PICO_INVALID_VALUE_IN_MIN_BUFFER": 0x00000137,
    "PICO_SIGGEN_FREQUENCY_OUT_OF_RANGE": 0x00000138,
    "PICO_EEPROM2_CORRUPT": 0x00000139,
    "PICO_EEPROM2_FAIL": 0x0000013A,
    "PICO_SERIAL_BUFFER_TOO_SMALL": 0x0000013B,
    "PICO_SIGGEN_TRIGGER_AND_EXTERNAL_CLOCK_CLASH": 0x0000013C,
    "PICO_WARNING_SIGGEN_AUXIO_TRIGGER_DISABLED": 0x0000013D,
    "PICO_SIGGEN_GATING_AUXIO_NOT_AVAILABLE": 0x00000013E,
    "PICO_SIGGEN_GATING_AUXIO_ENABLED": 0x00000013F,
    "PICO_DEVICE_TIME_STAMP_RESET": 0x01000000,
    "PICO_WATCHDOGTIMER": 0x10000000,
    "PICO_IPP_NOT_FOUND": 0x10000001,
    "PICO_IPP_NO_FUNCTION": 0x10000002,
    "PICO_IPP_ERROR": 0x10000003,
    "PICO_SHADOW_CAL_NOT_AVAILABLE": 0x10000004,
    "PICO_SHADOW_CAL_DISABLED": 0x10000005,
    "PICO_SHADOW_CAL_ERROR": 0x10000006,
    "PICO_SHADOW_CAL_CORRUPT": 0x10000007,
}

PICO_STATUS_LOOKUP = {v:k for k, v in PICO_STATUS.items()}

PICO_INFO = {
    "PICO_DRIVER_VERSION": 0x00000000,
    "PICO_USB_VERSION": 0x00000001,
    "PICO_HARDWARE_VERSION": 0x00000002,
    "PICO_VARIANT_INFO": 0x00000003,
    "PICO_BATCH_AND_SERIAL": 0x00000004,
    "PICO_CAL_DATE": 0x00000005,
    "PICO_KERNEL_VERSION": 0x00000006,
    "PICO_DIGITAL_HARDWARE_VERSION": 0x00000007,
    "PICO_ANALOGUE_HARDWARE_VERSION": 0x00000008,
    "PICO_FIRMWARE_VERSION_1": 0x00000009,
    "PICO_FIRMWARE_VERSION_2": 0x0000000A,
    "PICO_MAC_ADDRESS": 0x0000000B,
    "PICO_SHADOW_CAL": 0x0000000C,
    "PICO_IPP_VERSION": 0x0000000D,
}
