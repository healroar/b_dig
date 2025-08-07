import './App.css';
import "primereact/resources/themes/lara-light-cyan/theme.css";

import { InputText } from 'primereact/inputtext'
import { Menubar } from 'primereact/menubar';

function App() {
  return (
    <div className="flex flex-column gap-2">
        <label htmlFor="username">Username</label>
        <InputText id="username" aria-describedby="username-help" />
        <small id="username-help">
            Enter your username to reset your password.
        </small>
    </div>
  );
}

export default App;
