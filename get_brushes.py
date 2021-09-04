import os

# I'm downloading all files needed thius can work offline/in a sandbox
# After this script was run to get the pngs and glsl shaders, I replaced
# this.tiltShaderLoader.setPath("https://storage.googleapis.com/static.icosa.gallery/brushes/");
# with
# this.tiltShaderLoader.setPath("brushes/");

lines = open('icosa-viewer.module.js').readlines()
for l in lines:
    if '.glsl' in l: # Ditto for .png
        split = l.split('\"')
        if len(split)>1:
            print(len(split), split[1])
            os.system('mkdir -p brushes/'+split[1].split('/')[-2])
            os.system('curl https://storage.googleapis.com/static.icosa.gallery/brushes/'+split[1] +' > brushes/'+split[1])
