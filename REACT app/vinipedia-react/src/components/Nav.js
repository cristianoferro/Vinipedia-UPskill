import Link from "react-router-dom";

export default function Nav() {
  return (
    <div className="menu">
      <Link className="logo" to="/">
        <img src="/media/icons/Winecense_logo.png" />
      </Link>
      <Link className="menu-page" to="/">
        All Wines
      </Link>
    </div>
  );
}
