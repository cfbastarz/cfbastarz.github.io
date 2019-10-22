ruby -r rubygems -e 'require "jekyll-import";
    JekyllImport::Importers::WordpressDotCom.run({
      "source" => "/home/carlos/Downloads/alephzero.WordPress.2019-10-21.xml",
      "no_fetch_images" => false,
      "assets_folder" => "assets"
    })'
