export default function Homepage() {
  return (
    <div class="banner-trending">
      <img src="/media/7.jpg" />
      <h1 class="trending-message">
        <span>
          <strong>Trending portuguese wines</strong>
          <br />
          All over the world
        </span>
      </h1>
      <div class="attribution">
        <div class="attribution-detail">
          <div class="attribution-hidden">
            <p>
              Photo by{" "}
              <a class="author" href="author_url">
                {" "}
                X{" "}
              </a>
              from
              <a class="link-name" href="picture_url">
                {" "}
                X{" "}
              </a>
            </p>
          </div>
          <div class="attribution-icon">i</div>
        </div>
      </div>
    </div>
  );
}
