import search from "../media/icons/search.png";

export default function SearchBar() {
    return (
 
 <form className="search_box" method="get" action="" acceptCharset="UTF-8">
    <input class="search-button" type="image" src={search} value="Search">
  </form>

  );
}