// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_
#define AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "autopartol_interfaces/srv/detail/speech_text__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace autopartol_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpeechText_Request_text
{
public:
  Init_SpeechText_Request_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autopartol_interfaces::srv::SpeechText_Request text(::autopartol_interfaces::srv::SpeechText_Request::_text_type arg)
  {
    msg_.text = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autopartol_interfaces::srv::SpeechText_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::autopartol_interfaces::srv::SpeechText_Request>()
{
  return autopartol_interfaces::srv::builder::Init_SpeechText_Request_text();
}

}  // namespace autopartol_interfaces


namespace autopartol_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpeechText_Response_result
{
public:
  Init_SpeechText_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autopartol_interfaces::srv::SpeechText_Response result(::autopartol_interfaces::srv::SpeechText_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autopartol_interfaces::srv::SpeechText_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::autopartol_interfaces::srv::SpeechText_Response>()
{
  return autopartol_interfaces::srv::builder::Init_SpeechText_Response_result();
}

}  // namespace autopartol_interfaces

#endif  // AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_
