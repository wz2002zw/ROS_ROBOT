// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__TRAITS_HPP_
#define AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "autopartol_interfaces/srv/detail/speech_text__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace autopartol_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpeechText_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: text
  {
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpeechText_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: text
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpeechText_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace autopartol_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use autopartol_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const autopartol_interfaces::srv::SpeechText_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  autopartol_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use autopartol_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const autopartol_interfaces::srv::SpeechText_Request & msg)
{
  return autopartol_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<autopartol_interfaces::srv::SpeechText_Request>()
{
  return "autopartol_interfaces::srv::SpeechText_Request";
}

template<>
inline const char * name<autopartol_interfaces::srv::SpeechText_Request>()
{
  return "autopartol_interfaces/srv/SpeechText_Request";
}

template<>
struct has_fixed_size<autopartol_interfaces::srv::SpeechText_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autopartol_interfaces::srv::SpeechText_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autopartol_interfaces::srv::SpeechText_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace autopartol_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpeechText_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpeechText_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpeechText_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace autopartol_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use autopartol_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const autopartol_interfaces::srv::SpeechText_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  autopartol_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use autopartol_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const autopartol_interfaces::srv::SpeechText_Response & msg)
{
  return autopartol_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<autopartol_interfaces::srv::SpeechText_Response>()
{
  return "autopartol_interfaces::srv::SpeechText_Response";
}

template<>
inline const char * name<autopartol_interfaces::srv::SpeechText_Response>()
{
  return "autopartol_interfaces/srv/SpeechText_Response";
}

template<>
struct has_fixed_size<autopartol_interfaces::srv::SpeechText_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autopartol_interfaces::srv::SpeechText_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autopartol_interfaces::srv::SpeechText_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<autopartol_interfaces::srv::SpeechText>()
{
  return "autopartol_interfaces::srv::SpeechText";
}

template<>
inline const char * name<autopartol_interfaces::srv::SpeechText>()
{
  return "autopartol_interfaces/srv/SpeechText";
}

template<>
struct has_fixed_size<autopartol_interfaces::srv::SpeechText>
  : std::integral_constant<
    bool,
    has_fixed_size<autopartol_interfaces::srv::SpeechText_Request>::value &&
    has_fixed_size<autopartol_interfaces::srv::SpeechText_Response>::value
  >
{
};

template<>
struct has_bounded_size<autopartol_interfaces::srv::SpeechText>
  : std::integral_constant<
    bool,
    has_bounded_size<autopartol_interfaces::srv::SpeechText_Request>::value &&
    has_bounded_size<autopartol_interfaces::srv::SpeechText_Response>::value
  >
{
};

template<>
struct is_service<autopartol_interfaces::srv::SpeechText>
  : std::true_type
{
};

template<>
struct is_service_request<autopartol_interfaces::srv::SpeechText_Request>
  : std::true_type
{
};

template<>
struct is_service_response<autopartol_interfaces::srv::SpeechText_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__TRAITS_HPP_
