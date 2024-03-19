import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';


// Set up the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add lighting to the scene
const light = new THREE.HemisphereLight(0xffffff, 0x444444);
light.position.set(1, 1, 1);
scene.add(light);

// Instantiate a loader
const loader = new GLTFLoader();

// Load a glTF resource
loader.load(
  // resource URL
  '../uploads/box.gltf',
  // called when the resource is loaded
  function (gltf) {
    scene.add(gltf.scene);
    animate();
  },
  // called while loading is progressing
  function (xhr) {
    console.log((xhr.loaded / xhr.total * 100) + '% loaded');
  },
  // called when loading has errors
  function (error) {
    console.log('An error happened');
  }
);

// Set up the camera position
camera.position.z = 5;

// Create the animation loop
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

// Add orbit controls to allow user interaction
const controls = new OrbitControls(camera, renderer.domElement);

// Start the animation loop
animate();
