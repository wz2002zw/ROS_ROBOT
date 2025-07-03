// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_H_
#define AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'text'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SpeechText in the package autopartol_interfaces.
typedef struct autopartol_interfaces__srv__SpeechText_Request
{
  rosidl_runtime_c__String text;
} autopartol_interfaces__srv__SpeechText_Request;

// Struct for a sequence of autopartol_interfaces__srv__SpeechText_Request.
typedef struct autopartol_interfaces__srv__SpeechText_Request__Sequence
{
  autopartol_interfaces__srv__SpeechText_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autopartol_interfaces__srv__SpeechText_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SpeechText in the package autopartol_interfaces.
typedef struct autopartol_interfaces__srv__SpeechText_Response
{
  bool result;
} autopartol_interfaces__srv__SpeechText_Response;

// Struct for a sequence of autopartol_interfaces__srv__SpeechText_Response.
typedef struct autopartol_interfaces__srv__SpeechText_Response__Sequence
{
  autopartol_interfaces__srv__SpeechText_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autopartol_interfaces__srv__SpeechText_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_H_
