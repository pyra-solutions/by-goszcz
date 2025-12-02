{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell rec {
  buildInputs = with pkgs; [
    gcc
    clang
    go
    nodejs_22
    air

    # tooling
    gopls
    sqlite
    litecli
    postgresql_16
  ];
}
