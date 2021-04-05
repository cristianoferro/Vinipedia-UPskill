import styled from "styled-components";

export default function Homepage() {

    return(
        <StyledHomepage>
            <div class="banner-trending">
                <img src="/media/7.jpg" />
                <h1 class="trending-message">
                    <span>
                        <strong>Trending portuguese wines</strong>
                        <br/>
                        All over the world
                    </span>
                </h1>
                <div class="attribution">
                    <div class="attribution-detail">
                        <div class="attribution-hidden">
                            <p>Photo by <a class="author" href="author_url"> X </a>
                            from 
                            <a class="link-name" href="picture_url"> X </a></p>
                        </div>
                        <div class="attribution-icon">i</div>
                    </div>
                </div>
            </div>
        </StyledHomepage>
    )
}

const StyledHomepage = styled.div`
.banner-trending {
  height: 37.5vh;
  width: 100%;
  position: relative;
  overflow: hidden;
  justify-content: center;
  align-items: center;
  display: flex;
}

.banner-trending img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
}

.trending-message {
  z-index: 1;
  font-weight: 400;
  width: 100%;
  padding: 0 12.5vw;
  background-color: rgb(255, 255, 255, 0.7);
  height: 12.5vh;
  font-size: 1.5rem;
  color: #58595b;
  display: flex;
  align-items: center;
}`
;
