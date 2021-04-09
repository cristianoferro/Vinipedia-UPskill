import { Link } from "react-router-dom";
import Logo from "../media/icons/Winecense_logo.png";
import User from "../media/icons/user-icon.png";
import Button from "../media/icons/logout-icon.png";

export default function Nav() {
  return (
    <nav>
      <div className="menu">
        <Link className="logo" to="/">
          <img src={Logo} alt="logo" />
        </Link>
        <Link className="menu-page" to="/">
          All Wines
        </Link>
      </div>
      <div className="accounts-menu">
        <Link to="/">
          <img src={User} alt="user" />
        </Link>
        <Link to="/">
          <img src={Button} alt="logout btt" />
        </Link>
      </div>
    </nav>
  );
}
