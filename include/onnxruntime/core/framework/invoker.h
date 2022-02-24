// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#pragma once

namespace onnxruntime {
namespace invoker {

// todo: disable this when it is minimal build
int CreateEagerKernel(const void* execution_provier,
                      const char* op_name,
                      const char* domain,
                      const int& version,
                      const char** type_constraint_names,
                      const int* type_constraint_values,
                      const int& num_type_constraint,
                      const void* attrs,
                      const int& num_attrs,
                      void** kernel);

//int CallEagerKernel(const void* kernel, const void** inputs, const int& num_inputs, void** output, const int& num_outptus);

}//invoker
}//onnxruntime