// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autopartol_interfaces/srv/detail/speech_text__rosidl_typesupport_introspection_c.h"
#include "autopartol_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autopartol_interfaces/srv/detail/speech_text__functions.h"
#include "autopartol_interfaces/srv/detail/speech_text__struct.h"


// Include directives for member types
// Member `text`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autopartol_interfaces__srv__SpeechText_Request__init(message_memory);
}

void autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_fini_function(void * message_memory)
{
  autopartol_interfaces__srv__SpeechText_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_member_array[1] = {
  {
    "text",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autopartol_interfaces__srv__SpeechText_Request, text),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_members = {
  "autopartol_interfaces__srv",  // message namespace
  "SpeechText_Request",  // message name
  1,  // number of fields
  sizeof(autopartol_interfaces__srv__SpeechText_Request),
  autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_member_array,  // message members
  autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_type_support_handle = {
  0,
  &autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autopartol_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Request)() {
  if (!autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_type_support_handle.typesupport_identifier) {
    autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &autopartol_interfaces__srv__SpeechText_Request__rosidl_typesupport_introspection_c__SpeechText_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "autopartol_interfaces/srv/detail/speech_text__rosidl_typesupport_introspection_c.h"
// already included above
// #include "autopartol_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "autopartol_interfaces/srv/detail/speech_text__functions.h"
// already included above
// #include "autopartol_interfaces/srv/detail/speech_text__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autopartol_interfaces__srv__SpeechText_Response__init(message_memory);
}

void autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_fini_function(void * message_memory)
{
  autopartol_interfaces__srv__SpeechText_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_member_array[1] = {
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autopartol_interfaces__srv__SpeechText_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_members = {
  "autopartol_interfaces__srv",  // message namespace
  "SpeechText_Response",  // message name
  1,  // number of fields
  sizeof(autopartol_interfaces__srv__SpeechText_Response),
  autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_member_array,  // message members
  autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_type_support_handle = {
  0,
  &autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autopartol_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Response)() {
  if (!autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_type_support_handle.typesupport_identifier) {
    autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &autopartol_interfaces__srv__SpeechText_Response__rosidl_typesupport_introspection_c__SpeechText_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "autopartol_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "autopartol_interfaces/srv/detail/speech_text__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_members = {
  "autopartol_interfaces__srv",  // service namespace
  "SpeechText",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_Request_message_type_support_handle,
  NULL  // response message
  // autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_Response_message_type_support_handle
};

static rosidl_service_type_support_t autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_type_support_handle = {
  0,
  &autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autopartol_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText)() {
  if (!autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_type_support_handle.typesupport_identifier) {
    autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autopartol_interfaces, srv, SpeechText_Response)()->data;
  }

  return &autopartol_interfaces__srv__detail__speech_text__rosidl_typesupport_introspection_c__SpeechText_service_type_support_handle;
}
