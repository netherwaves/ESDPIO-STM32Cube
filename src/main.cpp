#include "daisy_seed.h"
#include "daisysp.h"

using namespace daisy;
using namespace daisysp;

Oscillator osc;
DaisySeed hw;

void AudioCallback(AudioHandle::InterleavingInputBuffer in, AudioHandle::InterleavingOutputBuffer out, size_t size)
{
  for (size_t i = 0; i < size; i += 2)
  {
    float samp = osc.Process();
    out[i] = out[i + 1] = samp * 0.05f;
  }
}

int main(void)
{
  hw.Init();
  hw.SetAudioBlockSize(4);
  float sample_rate = hw.AudioSampleRate();

  osc.Init(sample_rate);
  osc.SetAmp(1);
  osc.SetFreq(1000);
  osc.SetWaveform(Oscillator::WAVE_SIN);

  hw.StartAudio(AudioCallback);

  for(;;) {}
}