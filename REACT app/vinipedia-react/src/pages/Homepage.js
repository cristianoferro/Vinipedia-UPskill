import { Link } from "react-router-dom";
import Banner from "../media/banner.jpg";

export default function Homepage() {
  return (
    <div className="banner-trending">
      <img src={Banner} alt="Banner" />
      <h1 className="trending-message">
        <span>
          <strong>Trending portuguese wines</strong>
          <br />
          All over the world
        </span>
      </h1>
      <div className="attribution">
        <div className="attribution-detail">
          <div className="attribution-hidden">
            <p>
              Photo by{" "}
              <Link className="author" to="/">
                {" "}
                X{" "}
              </Link>
              from
              <Link className="link-name" to="/">
                {" "}
                X{" "}
              </Link>
            </p>
          </div>
          <div className="attribution-icon">i</div>
        </div>
      </div>
    </div>
  );
}
