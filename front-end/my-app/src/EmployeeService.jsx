import axios from 'axios'

class EmployeeService{

 async getEmployees(){
    return await axios.get('http://70.12.246.124:8080/admin/users/1' );
  }
}

export default new EmployeeService();