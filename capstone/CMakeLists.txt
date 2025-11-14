cmake_minimum_required(VERSION 3.8)
project(capstone)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install URDF/description files
install(DIRECTORY description
  DESTINATION share/${PROJECT_NAME}
)

# Install meshes (THIS IS CRITICAL)
install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}
)

# # Install worlds (optional)
# install(DIRECTORY worlds
#   DESTINATION share/${PROJECT_NAME}
# )

# # Install rviz config (optional)
# install(DIRECTORY rviz
#   DESTINATION share/${PROJECT_NAME}
# )

ament_package()