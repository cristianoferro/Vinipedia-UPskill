import Search from "../media/icons/search.png";

export default function SearchBar() {
  return (
    <form className="search_box" method="get" action="/" acceptCharset="UTF-8">
      <input type="text" placeholder="search" />
      <input
        className="search-button"
        type="image"
        src={Search}
        value="Search"
      />
    </form>
  );
}
