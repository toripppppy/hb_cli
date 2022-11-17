class HomebrewHbCli < Formula
  desc "Hit&Blowが遊べるスクリプト"
  homepage ""
  url "https://github.com/toripppppy/homebrew-hb_cli/releases/download/0.0.1/hbcli-1.0.tar.gz"
  sha256 "6d8333af0de53e056a3246c647485893ad98eb8e043089ba0c44716b6807bbab"

  def install
    bin.install "hb"
  end
end