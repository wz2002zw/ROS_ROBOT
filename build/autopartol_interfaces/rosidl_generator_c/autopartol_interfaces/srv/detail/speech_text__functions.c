// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autopartol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice
#include "autopartol_interfaces/srv/detail/speech_text__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `text`
#include "rosidl_runtime_c/string_functions.h"

bool
autopartol_interfaces__srv__SpeechText_Request__init(autopartol_interfaces__srv__SpeechText_Request * msg)
{
  if (!msg) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__init(&msg->text)) {
    autopartol_interfaces__srv__SpeechText_Request__fini(msg);
    return false;
  }
  return true;
}

void
autopartol_interfaces__srv__SpeechText_Request__fini(autopartol_interfaces__srv__SpeechText_Request * msg)
{
  if (!msg) {
    return;
  }
  // text
  rosidl_runtime_c__String__fini(&msg->text);
}

bool
autopartol_interfaces__srv__SpeechText_Request__are_equal(const autopartol_interfaces__srv__SpeechText_Request * lhs, const autopartol_interfaces__srv__SpeechText_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->text), &(rhs->text)))
  {
    return false;
  }
  return true;
}

bool
autopartol_interfaces__srv__SpeechText_Request__copy(
  const autopartol_interfaces__srv__SpeechText_Request * input,
  autopartol_interfaces__srv__SpeechText_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__copy(
      &(input->text), &(output->text)))
  {
    return false;
  }
  return true;
}

autopartol_interfaces__srv__SpeechText_Request *
autopartol_interfaces__srv__SpeechText_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Request * msg = (autopartol_interfaces__srv__SpeechText_Request *)allocator.allocate(sizeof(autopartol_interfaces__srv__SpeechText_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autopartol_interfaces__srv__SpeechText_Request));
  bool success = autopartol_interfaces__srv__SpeechText_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
autopartol_interfaces__srv__SpeechText_Request__destroy(autopartol_interfaces__srv__SpeechText_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    autopartol_interfaces__srv__SpeechText_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
autopartol_interfaces__srv__SpeechText_Request__Sequence__init(autopartol_interfaces__srv__SpeechText_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Request * data = NULL;

  if (size) {
    data = (autopartol_interfaces__srv__SpeechText_Request *)allocator.zero_allocate(size, sizeof(autopartol_interfaces__srv__SpeechText_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autopartol_interfaces__srv__SpeechText_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autopartol_interfaces__srv__SpeechText_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
autopartol_interfaces__srv__SpeechText_Request__Sequence__fini(autopartol_interfaces__srv__SpeechText_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autopartol_interfaces__srv__SpeechText_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

autopartol_interfaces__srv__SpeechText_Request__Sequence *
autopartol_interfaces__srv__SpeechText_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Request__Sequence * array = (autopartol_interfaces__srv__SpeechText_Request__Sequence *)allocator.allocate(sizeof(autopartol_interfaces__srv__SpeechText_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = autopartol_interfaces__srv__SpeechText_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
autopartol_interfaces__srv__SpeechText_Request__Sequence__destroy(autopartol_interfaces__srv__SpeechText_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    autopartol_interfaces__srv__SpeechText_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
autopartol_interfaces__srv__SpeechText_Request__Sequence__are_equal(const autopartol_interfaces__srv__SpeechText_Request__Sequence * lhs, const autopartol_interfaces__srv__SpeechText_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!autopartol_interfaces__srv__SpeechText_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
autopartol_interfaces__srv__SpeechText_Request__Sequence__copy(
  const autopartol_interfaces__srv__SpeechText_Request__Sequence * input,
  autopartol_interfaces__srv__SpeechText_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(autopartol_interfaces__srv__SpeechText_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    autopartol_interfaces__srv__SpeechText_Request * data =
      (autopartol_interfaces__srv__SpeechText_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!autopartol_interfaces__srv__SpeechText_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          autopartol_interfaces__srv__SpeechText_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!autopartol_interfaces__srv__SpeechText_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
autopartol_interfaces__srv__SpeechText_Response__init(autopartol_interfaces__srv__SpeechText_Response * msg)
{
  if (!msg) {
    return false;
  }
  // result
  return true;
}

void
autopartol_interfaces__srv__SpeechText_Response__fini(autopartol_interfaces__srv__SpeechText_Response * msg)
{
  if (!msg) {
    return;
  }
  // result
}

bool
autopartol_interfaces__srv__SpeechText_Response__are_equal(const autopartol_interfaces__srv__SpeechText_Response * lhs, const autopartol_interfaces__srv__SpeechText_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // result
  if (lhs->result != rhs->result) {
    return false;
  }
  return true;
}

bool
autopartol_interfaces__srv__SpeechText_Response__copy(
  const autopartol_interfaces__srv__SpeechText_Response * input,
  autopartol_interfaces__srv__SpeechText_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // result
  output->result = input->result;
  return true;
}

autopartol_interfaces__srv__SpeechText_Response *
autopartol_interfaces__srv__SpeechText_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Response * msg = (autopartol_interfaces__srv__SpeechText_Response *)allocator.allocate(sizeof(autopartol_interfaces__srv__SpeechText_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autopartol_interfaces__srv__SpeechText_Response));
  bool success = autopartol_interfaces__srv__SpeechText_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
autopartol_interfaces__srv__SpeechText_Response__destroy(autopartol_interfaces__srv__SpeechText_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    autopartol_interfaces__srv__SpeechText_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
autopartol_interfaces__srv__SpeechText_Response__Sequence__init(autopartol_interfaces__srv__SpeechText_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Response * data = NULL;

  if (size) {
    data = (autopartol_interfaces__srv__SpeechText_Response *)allocator.zero_allocate(size, sizeof(autopartol_interfaces__srv__SpeechText_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autopartol_interfaces__srv__SpeechText_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autopartol_interfaces__srv__SpeechText_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
autopartol_interfaces__srv__SpeechText_Response__Sequence__fini(autopartol_interfaces__srv__SpeechText_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autopartol_interfaces__srv__SpeechText_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

autopartol_interfaces__srv__SpeechText_Response__Sequence *
autopartol_interfaces__srv__SpeechText_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  autopartol_interfaces__srv__SpeechText_Response__Sequence * array = (autopartol_interfaces__srv__SpeechText_Response__Sequence *)allocator.allocate(sizeof(autopartol_interfaces__srv__SpeechText_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = autopartol_interfaces__srv__SpeechText_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
autopartol_interfaces__srv__SpeechText_Response__Sequence__destroy(autopartol_interfaces__srv__SpeechText_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    autopartol_interfaces__srv__SpeechText_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
autopartol_interfaces__srv__SpeechText_Response__Sequence__are_equal(const autopartol_interfaces__srv__SpeechText_Response__Sequence * lhs, const autopartol_interfaces__srv__SpeechText_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!autopartol_interfaces__srv__SpeechText_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
autopartol_interfaces__srv__SpeechText_Response__Sequence__copy(
  const autopartol_interfaces__srv__SpeechText_Response__Sequence * input,
  autopartol_interfaces__srv__SpeechText_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(autopartol_interfaces__srv__SpeechText_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    autopartol_interfaces__srv__SpeechText_Response * data =
      (autopartol_interfaces__srv__SpeechText_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!autopartol_interfaces__srv__SpeechText_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          autopartol_interfaces__srv__SpeechText_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!autopartol_interfaces__srv__SpeechText_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
