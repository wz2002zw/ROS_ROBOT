// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_
#define AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__autopartol_interfaces__srv__SpeechText_Request __attribute__((deprecated))
#else
# define DEPRECATED__autopartol_interfaces__srv__SpeechText_Request __declspec(deprecated)
#endif

namespace autopartol_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SpeechText_Request_
{
  using Type = SpeechText_Request_<ContainerAllocator>;

  explicit SpeechText_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->text = "";
    }
  }

  explicit SpeechText_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : text(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->text = "";
    }
  }

  // field types and members
  using _text_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _text_type text;

  // setters for named parameter idiom
  Type & set__text(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->text = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autopartol_interfaces__srv__SpeechText_Request
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autopartol_interfaces__srv__SpeechText_Request
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SpeechText_Request_ & other) const
  {
    if (this->text != other.text) {
      return false;
    }
    return true;
  }
  bool operator!=(const SpeechText_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SpeechText_Request_

// alias to use template instance with default allocator
using SpeechText_Request =
  autopartol_interfaces::srv::SpeechText_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace autopartol_interfaces


#ifndef _WIN32
# define DEPRECATED__autopartol_interfaces__srv__SpeechText_Response __attribute__((deprecated))
#else
# define DEPRECATED__autopartol_interfaces__srv__SpeechText_Response __declspec(deprecated)
#endif

namespace autopartol_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SpeechText_Response_
{
  using Type = SpeechText_Response_<ContainerAllocator>;

  explicit SpeechText_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  explicit SpeechText_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  // field types and members
  using _result_type =
    bool;
  _result_type result;

  // setters for named parameter idiom
  Type & set__result(
    const bool & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autopartol_interfaces__srv__SpeechText_Response
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autopartol_interfaces__srv__SpeechText_Response
    std::shared_ptr<autopartol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SpeechText_Response_ & other) const
  {
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const SpeechText_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SpeechText_Response_

// alias to use template instance with default allocator
using SpeechText_Response =
  autopartol_interfaces::srv::SpeechText_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace autopartol_interfaces

namespace autopartol_interfaces
{

namespace srv
{

struct SpeechText
{
  using Request = autopartol_interfaces::srv::SpeechText_Request;
  using Response = autopartol_interfaces::srv::SpeechText_Response;
};

}  // namespace srv

}  // namespace autopartol_interfaces

#endif  // AUTOPARTOL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_
