{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.hello
    pkgs.python3

    # keep this line if you use bash
    pkgs.bashInteractive
  ];

  shellHook = ''
    PATH=./../go/bin:$PATH
  '';

}
